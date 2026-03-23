"""
app_ui_vintage.py
-----------------
Flask web interface — vintage typewriter aesthetic.
Usage: python app_ui_vintage.py
"""

import os
from flask import Flask, request, jsonify, render_template_string
from query import RAGEngine
from config import APP_NAME, APP_SHORT_NAME, PORT, SUGGESTIONS, LLM_PROVIDER, LLM_MODEL

app = Flask(__name__)

engine = None
engine_error = None
try:
    engine = RAGEngine()
except Exception as e:
    engine_error = str(e)
    print(f"[!] Engine error: {e}")


HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ app_name }}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

:root{
  --paper:     #f5f0e8;
  --paper2:    #ede8da;
  --paper3:    #e4dece;
  --ink:       #1a1410;
  --ink2:      #4a3f35;
  --ink3:      #8a7a6a;
  --red:       #8b2020;
  --border:    #c8b99a;
  --shadow:    rgba(26,20,16,0.12);
  --display:   'Special Elite', cursive;
  --mono:      'Courier Prime', monospace;
}

html,body{height:100%;overflow:hidden}

body{
  font-family:var(--mono);
  background:var(--paper3);
  color:var(--ink);
  display:flex;
  flex-direction:column;
}

/* ── Paper grain texture ── */
body::before{
  content:'';
  position:fixed;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events:none;z-index:0;opacity:0.6;
}

/* ── Horizontal rules as decorative lines ── */
.rule{
  border:none;
  border-top:1px solid var(--border);
  margin:0;
}
.rule.double{
  border-top:3px double var(--border);
}

/* ── Header ── */
header{
  position:relative;z-index:10;
  background:var(--paper);
  border-bottom:3px double var(--border);
  padding:0 32px;
  flex-shrink:0;
}

.header-top{
  display:flex;align-items:center;justify-content:space-between;
  padding:10px 0 6px;
}

.masthead{
  font-family:var(--display);
  font-size:22px;
  letter-spacing:0.04em;
  color:var(--ink);
}

.masthead span{
  font-family:var(--mono);
  font-size:10px;
  font-weight:700;
  letter-spacing:0.2em;
  text-transform:uppercase;
  color:var(--ink3);
  display:block;
  margin-bottom:2px;
}

.header-meta{
  font-family:var(--mono);
  font-size:10px;
  color:var(--ink3);
  text-align:right;
  line-height:1.6;
  letter-spacing:0.05em;
}

.header-bottom{
  display:flex;align-items:center;justify-content:space-between;
  padding:4px 0 8px;
  font-size:10px;
  color:var(--ink3);
  letter-spacing:0.08em;
  text-transform:uppercase;
}

.status-ok  { color: #2a5a2a; }
.status-err { color: var(--red); }

/* ── Main layout ── */
.main{
  position:relative;z-index:1;
  flex:1;display:flex;flex-direction:column;
  max-width:820px;width:100%;
  margin:0 auto;padding:0 24px;
  overflow:hidden;
}

/* ── Welcome ── */
#welcome{
  flex:1;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  gap:16px;text-align:center;padding:32px 0;
}

.welcome-title{
  font-family:var(--display);
  font-size:28px;
  color:var(--ink);
  line-height:1.3;
}

.welcome-sub{
  font-size:12px;color:var(--ink3);
  max-width:400px;line-height:1.8;
  letter-spacing:0.03em;
}

.welcome-divider{
  font-family:var(--mono);
  font-size:11px;color:var(--border);
  letter-spacing:0.3em;
  margin:4px 0;
}

.suggestion-grid{
  display:grid;grid-template-columns:1fr 1fr;
  gap:8px;width:100%;max-width:540px;
  margin-top:8px;
}

.suggestion{
  background:var(--paper);
  border:1px solid var(--border);
  padding:10px 14px;
  font-family:var(--mono);
  font-size:11px;color:var(--ink2);
  cursor:pointer;text-align:left;
  line-height:1.6;
  transition:background .15s,border-color .15s;
  position:relative;
}
.suggestion::before{
  content:'›';
  position:absolute;left:6px;top:10px;
  color:var(--border);font-size:13px;
}
.suggestion{padding-left:18px}
.suggestion:hover{
  background:var(--paper2);
  border-color:var(--ink3);
  color:var(--ink);
}

/* ── Chat ── */
#chat{
  flex:1;overflow-y:auto;
  padding:20px 0 8px;
  display:flex;flex-direction:column;gap:0;
  scroll-behavior:smooth;
}
#chat::-webkit-scrollbar{width:4px}
#chat::-webkit-scrollbar-thumb{background:var(--border)}

.msg{
  display:flex;flex-direction:column;
  padding:14px 0;
  border-bottom:1px dashed var(--border);
  animation:fadeIn .2s ease both;
}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}

.msg-header{
  display:flex;align-items:baseline;gap:10px;
  margin-bottom:8px;
}

.msg-label{
  font-family:var(--display);
  font-size:13px;color:var(--ink);
}

.msg.user .msg-label{ color: var(--red); }

.msg-line{
  font-family:var(--mono);font-size:9px;
  color:var(--border);letter-spacing:0.15em;
  text-transform:uppercase;flex:1;
  border-bottom:1px solid var(--border);
  margin-bottom:2px;
}

.msg-bubble{
  font-family:var(--mono);
  font-size:13px;line-height:1.9;
  color:var(--ink2);
  padding-left:2px;
}

.msg-bubble p{
  margin-bottom:1em;
}
.msg-bubble p:last-child{
  margin-bottom:0;
}

.msg.user .msg-bubble{
  color:var(--ink);
  font-style:italic;
}

.msg.error .msg-bubble{ color:var(--red); }

/* ── Thinking ── */
.thinking .msg-bubble{
  color:var(--ink3);
  font-style:italic;
}
.cursor-blink{
  display:inline-block;
  width:8px;height:13px;
  background:var(--ink3);
  margin-left:2px;
  vertical-align:text-bottom;
  animation:blink .8s step-end infinite;
}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

/* ── Sources ── */
.sources{
  display:flex;flex-wrap:wrap;gap:6px;
  margin-top:10px;padding-top:8px;
  border-top:1px dashed var(--border);
}
.source-tag{
  font-family:var(--mono);font-size:9px;
  color:var(--ink3);letter-spacing:0.08em;
  text-transform:uppercase;
}
.source-tag::before{content:'[ref: '}
.source-tag::after{content:']'}

/* ── Input bar ── */
.input-wrap{
  flex-shrink:0;
  padding:12px 0 16px;
  border-top:3px double var(--border);
}

.input-prompt-row{
  display:flex;align-items:flex-start;gap:0;
}

.prompt-gutter{
  font-family:var(--display);
  font-size:16px;color:var(--ink3);
  padding:8px 10px 0 0;
  flex-shrink:0;
  user-select:none;
}

textarea{
  flex:1;
  background:transparent;
  border:none;border-bottom:1px solid var(--ink3);
  outline:none;
  color:var(--ink);
  font-family:var(--mono);
  font-size:13px;
  line-height:1.7;
  resize:none;
  min-height:28px;max-height:120px;
  padding:4px 0;
  letter-spacing:0.02em;
  transition:border-color .15s;
}
textarea:focus{border-bottom-color:var(--ink)}
textarea::placeholder{color:var(--ink3);font-style:italic}

.send-btn{
  background:transparent;
  border:1px solid var(--ink3);
  color:var(--ink2);
  font-family:var(--display);
  font-size:12px;
  letter-spacing:0.1em;
  padding:6px 14px;
  cursor:pointer;
  margin-left:12px;margin-top:4px;
  flex-shrink:0;
  transition:background .15s,color .15s;
  text-transform:uppercase;
}
.send-btn:hover{background:var(--ink);color:var(--paper)}
.send-btn:disabled{opacity:.4;cursor:default}

.input-footer{
  display:flex;justify-content:space-between;
  margin-top:6px;
  font-size:9px;color:var(--ink3);
  letter-spacing:0.1em;text-transform:uppercase;
}

/* ── Error banner ── */
.engine-error{
  border:1px solid var(--red);
  padding:12px 16px;margin:16px 0;
  font-size:12px;color:var(--red);line-height:1.7;
  font-family:var(--mono);
}
.engine-error code{font-weight:700}
</style>
</head>
<body>

<header>
  <div class="header-top">
    <div class="masthead">
      <span>Document Intelligence System</span>
      {{ app_name }}
    </div>
    <div class="header-meta">
      {{ provider|upper }} / {{ model }}<br>
      {% if engine_ready %}
      <span class="status-ok">■ INDEX READY</span>
      {% else %}
      <span class="status-err">■ INDEX NOT FOUND</span>
      {% endif %}
    </div>
  </div>
  <div class="rule double"></div>
  <div class="header-bottom">
    <span>Query Interface v1.0</span>
    <span>Retrieval-Augmented Generation</span>
    <span>{{ provider|upper }} Engine</span>
  </div>
</header>

<div class="main">

  {% if not engine_ready %}
  <div class="engine-error">
    !! INDEX NOT LOADED — Run <code>python ingest.py</code> then restart.<br>
    Error: {{ engine_error }}
  </div>
  {% endif %}

  <div id="welcome">
    <div class="welcome-divider">— ✦ —</div>
    <div class="welcome-title">What shall we find<br>in your documents?</div>
    <div class="welcome-sub">Type your query below, or select a prompt to begin.<br>All answers drawn directly from your documents.</div>
    <div class="welcome-divider">- - - - - - - - - - - - - - - - - - - -</div>
    <div class="suggestion-grid">
      {% for s in suggestions %}
      <div class="suggestion" onclick="useSuggestion(this)">{{ s }}</div>
      {% endfor %}
    </div>
  </div>

  <div id="chat" style="display:none"></div>

  <div class="input-wrap">
    <div class="input-prompt-row">
      <div class="prompt-gutter">&gt;</div>
      <textarea id="input"
        placeholder="Type your query here..."
        rows="1"
        {% if not engine_ready %}disabled{% endif %}
        onkeydown="handleKey(event)"
        oninput="autoResize(this)"></textarea>
      <button class="send-btn" id="send-btn"
        {% if not engine_ready %}disabled{% endif %}
        onclick="sendMessage()">Send</button>
    </div>
    <div class="input-footer">
      <span>Enter to send · Shift+Enter for new line</span>
      <span>Top-K retrieval active</span>
    </div>
  </div>

</div>

<script>
const chatEl=document.getElementById('chat'),welcomeEl=document.getElementById('welcome');
const inputEl=document.getElementById('input'),sendBtn=document.getElementById('send-btn');
let busy=false;

function useSuggestion(el){inputEl.value=el.textContent.trim();autoResize(inputEl);sendMessage()}
function autoResize(el){el.style.height='auto';el.style.height=Math.min(el.scrollHeight,120)+'px'}
function handleKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMessage()}}

function now(){
  return new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'});
}

function addMsg(role,text,sources){
  const div=document.createElement('div');
  div.className=`msg ${role}`;

  const hdr=document.createElement('div');
  hdr.className='msg-header';

  const lbl=document.createElement('div');
  lbl.className='msg-label';
  lbl.textContent = role==='user' ? 'Query' : (role==='bot'||role==='thinking') ? 'Response' : 'Error';

  const line=document.createElement('div');
  line.className='msg-line';

  hdr.appendChild(lbl);
  hdr.appendChild(line);

  const bubble=document.createElement('div');
  bubble.className='msg-bubble';

  if(role==='thinking'){
    div.className='msg bot thinking';
    bubble.innerHTML='Searching documents<span class="cursor-blink"></span>';
  } else {
    const paras = text.split(/\n\n+/);
    bubble.innerHTML = paras.map(p => `<p>${p.replace(/\n/g,'<br>')}</p>`).join('');
  }

  div.appendChild(hdr);
  div.appendChild(bubble);

  if(sources&&sources.length){
    const srcs=document.createElement('div');
    srcs.className='sources';
    const seen=new Set();
    sources.forEach(s=>{
      const k=`${s.source}:${s.page}`;
      if(seen.has(k))return;seen.add(k);
      const t=document.createElement('div');
      t.className='source-tag';
      t.textContent=`${s.source} p.${s.page}`;
      srcs.appendChild(t);
    });
    div.appendChild(srcs);
  }

  chatEl.appendChild(div);
  chatEl.scrollTop=chatEl.scrollHeight;
  return div;
}

async function sendMessage(){
  const q=inputEl.value.trim();
  if(!q||busy)return;
  busy=true;

  welcomeEl.style.display='none';
  chatEl.style.display='flex';

  inputEl.value='';autoResize(inputEl);
  sendBtn.disabled=true;

  addMsg('user',q);
  const thinking=addMsg('thinking','');

  try{
    const res=await fetch('/ask',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({question:q})
    });
    const data=await res.json();
    thinking.remove();
    if(data.error) addMsg('error',data.error);
    else addMsg('bot',data.answer,data.sources);
  }catch(err){
    thinking.remove();
    addMsg('error','Network error. Is the server running?');
  }

  busy=false;sendBtn.disabled=false;inputEl.focus();
}
</script>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(
        HTML,
        app_name=APP_NAME,
        short_name=APP_SHORT_NAME,
        provider=LLM_PROVIDER,
        model=LLM_MODEL,
        engine_ready=(engine is not None),
        engine_error=engine_error or "",
        suggestions=SUGGESTIONS,
    )


@app.route("/ask", methods=["POST"])
def ask():
    if engine is None:
        return jsonify({"error": f"Index not loaded. Run ingest.py first. ({engine_error})"}), 503

    data     = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "No question provided."}), 400

    try:
        chunks  = engine.retrieve(question)
        context = engine.build_context(chunks)
        answer  = engine.ask(question)
        sources = [{"source": c["source"], "page": c["page"]} for c in chunks]
        return jsonify({"answer": answer, "sources": sources})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print(f"\n[✓] {APP_NAME} running at http://localhost:{PORT}\n")
    app.run(host="0.0.0.0", port=PORT, debug=False)

"""
app_ui.py
---------
Flask web interface. Reads branding and settings from config.py.

Usage:
    python app_ui.py
    Open http://localhost:5000
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
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Sora:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  :root{
    --bg:#0d0f14;--surface:#13161e;--surface2:#1a1e2a;
    --border:#252a38;--accent:#3d8bff;--accent2:#5eead4;
    --text:#e2e8f4;--text2:#7c87a0;--text3:#4a5268;
    --user-bg:#1c2340;--bot-bg:#131720;--danger:#f87171;
    --mono:'DM Mono',monospace;--sans:'Sora',sans-serif;--r:12px;
  }
  html,body{height:100%;overflow:hidden}
  body{font-family:var(--sans);background:var(--bg);color:var(--text);display:flex;flex-direction:column}
  body::before{
    content:'';position:fixed;inset:0;
    background-image:linear-gradient(var(--border)1px,transparent 1px),linear-gradient(90deg,var(--border)1px,transparent 1px);
    background-size:48px 48px;opacity:0.18;pointer-events:none;z-index:0;
  }
  header{
    position:relative;z-index:10;display:flex;align-items:center;justify-content:space-between;
    padding:0 28px;height:56px;border-bottom:1px solid var(--border);
    background:rgba(13,15,20,0.92);backdrop-filter:blur(12px);flex-shrink:0;
  }
  .logo{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--text2)}
  .logo-mark{width:28px;height:28px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;letter-spacing:0}
  .meta{display:flex;align-items:center;gap:10px}
  .model-tag{font-family:var(--mono);font-size:10px;color:var(--text3);padding:3px 8px;border:1px solid var(--border);border-radius:20px}
  .status-pill{font-family:var(--mono);font-size:11px;padding:4px 10px;border-radius:20px;border:1px solid}
  .status-pill.ok{color:var(--accent2);border-color:rgba(94,234,212,.25);background:rgba(94,234,212,.06)}
  .status-pill.error{color:var(--danger);border-color:rgba(248,113,113,.25);background:rgba(248,113,113,.06)}
  .main{position:relative;z-index:1;flex:1;display:flex;flex-direction:column;max-width:860px;width:100%;margin:0 auto;padding:0 20px;overflow:hidden}
  #welcome{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;padding:40px 0}
  .welcome-icon{width:56px;height:56px;background:linear-gradient(135deg,rgba(61,139,255,.15),rgba(94,234,212,.15));border:1px solid var(--border);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:4px}
  #welcome h1{font-size:22px;font-weight:600}
  #welcome p{font-size:14px;color:var(--text2);max-width:420px;line-height:1.6}
  .suggestion-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px;width:100%;max-width:560px}
  .suggestion{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:12px 14px;font-size:12px;color:var(--text2);cursor:pointer;text-align:left;transition:border-color .15s,color .15s,background .15s;line-height:1.5}
  .suggestion:hover{border-color:var(--accent);color:var(--text);background:var(--surface2)}
  #chat{flex:1;overflow-y:auto;padding:24px 0 12px;display:flex;flex-direction:column;gap:20px;scroll-behavior:smooth}
  #chat::-webkit-scrollbar{width:4px}
  #chat::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
  .msg{display:flex;flex-direction:column;gap:4px;animation:fadeUp .2s ease both}
  @keyframes fadeUp{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
  .msg-label{font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);padding:0 2px}
  .msg.user .msg-label{color:rgba(61,139,255,.6)}
  .msg-bubble{padding:14px 16px;border-radius:var(--r);font-size:14px;line-height:1.75;border:1px solid var(--border)}
  .msg.user .msg-bubble{background:var(--user-bg);border-color:rgba(61,139,255,.2)}
  .msg.bot  .msg-bubble{background:var(--bot-bg);white-space:pre-wrap}
  .msg.error .msg-bubble{background:rgba(248,113,113,.05);border-color:rgba(248,113,113,.2);color:var(--danger)}
  .sources{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
  .source-tag{font-family:var(--mono);font-size:10px;color:var(--text3);background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:3px 8px}
  .source-tag span{color:var(--accent2)}
  .thinking .msg-bubble{display:flex;align-items:center;gap:8px;color:var(--text2);font-size:13px}
  .dots{display:flex;gap:4px}
  .dots span{width:5px;height:5px;background:var(--text3);border-radius:50%;animation:blink 1.2s ease infinite}
  .dots span:nth-child(2){animation-delay:.2s}
  .dots span:nth-child(3){animation-delay:.4s}
  @keyframes blink{0%,80%,100%{opacity:.2;transform:scale(.8)}40%{opacity:1;transform:scale(1)}}
  .input-wrap{flex-shrink:0;padding:14px 0 20px}
  .input-row{display:flex;align-items:flex-end;gap:8px;background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:8px 8px 8px 16px;transition:border-color .15s}
  .input-row:focus-within{border-color:rgba(61,139,255,.5)}
  textarea{flex:1;background:transparent;border:none;outline:none;color:var(--text);font-family:var(--sans);font-size:14px;line-height:1.5;resize:none;min-height:24px;max-height:140px;padding:4px 0}
  textarea::placeholder{color:var(--text3)}
  .send-btn{width:36px;height:36px;flex-shrink:0;background:var(--accent);border:none;border-radius:10px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s,opacity .15s;color:#fff}
  .send-btn:hover{background:#5a9fff}
  .send-btn:disabled{opacity:.35;cursor:default}
  .send-btn svg{width:16px;height:16px}
  .input-hint{font-size:10px;color:var(--text3);text-align:center;margin-top:8px;font-family:var(--mono)}
  .engine-error{background:rgba(248,113,113,.06);border:1px solid rgba(248,113,113,.2);border-radius:var(--r);padding:14px 16px;margin:16px 0;font-size:13px;color:var(--danger);line-height:1.6}
  .engine-error code{font-family:var(--mono);font-size:12px;background:rgba(248,113,113,.1);padding:2px 6px;border-radius:4px}
</style>
</head>
<body>
<header>
  <div class="logo">
    <div class="logo-mark">{{ short_name }}</div>
    {{ app_name }}
  </div>
  <div class="meta">
    <div class="model-tag">{{ provider }}/{{ model }}</div>
    {% if engine_ready %}
    <div class="status-pill ok">● Index loaded</div>
    {% else %}
    <div class="status-pill error">● Index not found</div>
    {% endif %}
  </div>
</header>

<div class="main">
  {% if not engine_ready %}
  <div class="engine-error">
    <strong>Index not ready.</strong><br>
    Run <code>python ingest.py</code> then restart this server.<br>
    Error: {{ engine_error }}
  </div>
  {% endif %}

  <div id="welcome">
    <div class="welcome-icon">&#128188;</div>
    <h1>BRELA &amp; TRA Business Assistant</h1>
    <p>Ask any question about business registration, licensing, or taxation in Tanzania. Answers are sourced directly from official BRELA and TRA documents.</p>
    <div class="suggestion-grid">
      {% for s in suggestions %}
      <div class="suggestion" onclick="useSuggestion(this)">{{ s }}</div>
      {% endfor %}
    </div>
  </div>

  <div id="chat" style="display:none"></div>

  <div class="input-wrap">
    <div class="input-row">
      <textarea id="input" placeholder="Ask about business registration, licensing, or taxation…" rows="1"
        {% if not engine_ready %}disabled{% endif %}
        onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
      <button class="send-btn" id="send-btn"
        {% if not engine_ready %}disabled{% endif %}
        onclick="sendMessage()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/>
        </svg>
      </button>
    </div>
    <div class="input-hint">Enter to send · Shift+Enter for new line</div>
  </div>
</div>

<script>
const chatEl=document.getElementById('chat'),welcomeEl=document.getElementById('welcome'),inputEl=document.getElementById('input'),sendBtn=document.getElementById('send-btn');
let busy=false;
function useSuggestion(el){inputEl.value=el.textContent;autoResize(inputEl);sendMessage()}
function autoResize(el){el.style.height='auto';el.style.height=Math.min(el.scrollHeight,140)+'px'}
function handleKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMessage()}}
function addMsg(role,text,sources){
  const div=document.createElement('div');div.className=`msg ${role}`;
  const lbl=document.createElement('div');lbl.className='msg-label';
  lbl.textContent=role==='user'?'You':role==='bot'?'Assistant':'Error';
  const bubble=document.createElement('div');bubble.className='msg-bubble';
  if(role==='thinking'){div.className='msg bot thinking';lbl.textContent='Assistant';bubble.innerHTML='<div class="dots"><span></span><span></span><span></span></div> Searching documents…'}
  else{bubble.textContent=text}
  div.appendChild(lbl);div.appendChild(bubble);
  if(sources&&sources.length){
    const srcs=document.createElement('div');srcs.className='sources';
    const seen=new Set();
    sources.forEach(s=>{const k=`${s.source}:${s.page}`;if(seen.has(k))return;seen.add(k);const t=document.createElement('div');t.className='source-tag';t.innerHTML=`${s.source} · p.<span>${s.page}</span>`;srcs.appendChild(t)});
    div.appendChild(srcs);
  }
  chatEl.appendChild(div);chatEl.scrollTop=chatEl.scrollHeight;return div;
}
async function sendMessage(){
  const q=inputEl.value.trim();if(!q||busy)return;busy=true;
  welcomeEl.style.display='none';chatEl.style.display='flex';
  inputEl.value='';autoResize(inputEl);sendBtn.disabled=true;
  addMsg('user',q);const thinking=addMsg('thinking','');
  try{
    const res=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q})});
    const data=await res.json();thinking.remove();
    if(data.error)addMsg('error',data.error);
    else addMsg('bot',data.answer,data.sources);
  }catch(err){thinking.remove();addMsg('error','Network error.')}
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
        result  = engine.ask(question)
        return jsonify({"answer": result["answer"], "sources": result["sources"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print(f"\n[✓] {APP_NAME} running at http://localhost:{PORT}\n")
    app.run(host="0.0.0.0", port=PORT, debug=False)

"""
knowledge_base.py
-----------------
Manual knowledge entries for BRELA & TRA topics not covered by uploaded PDFs.

HOW TO ADD AN ENTRY:
    {
        "topic":    "Short title for this entry",
        "content":  "The full explanation, rules, or instructions.",
        "keywords": ["word1", "word2", ...]   # words that trigger this entry
    }

Keywords are matched against the user's question (case-insensitive).
An entry is included in the context if ANY of its keywords appear in the question.
"""

ENTRIES = [

    # ── BRELA ────────────────────────────────────────────────────────────────

    {
        "topic": "BRELA Online Registration Portal",
        "content": (
            "BRELA's online business registration portal is accessible at "
            "https://ors.brela.go.tz. New users must create an account before "
            "submitting any registration application. All submissions, payments, "
            "and certificate downloads are handled through this portal."
        ),
        "keywords": ["brela", "portal", "online", "register", "registration", "website", "ors"],
    },

    {
        "topic": "Company Name Reservation",
        "content": (
            "Before registering a company, applicants must reserve a company name "
            "through BRELA. A name reservation is valid for 30 days. The reservation "
            "fee is TZS 10,000. The proposed name must not be identical or similar to "
            "an already registered entity and must not contain restricted words such as "
            "'Government', 'National', or 'Bank' without prior approval."
        ),
        "keywords": ["name", "reservation", "reserve", "company name", "brela"],
    },

    {
        "topic": "Types of Business Entities Registered by BRELA",
        "content": (
            "BRELA registers the following types of business entities in Tanzania: "
            "1. Private Limited Company (Ltd) — minimum 1 shareholder, maximum 50. "
            "2. Public Limited Company (PLC) — minimum 7 shareholders, no maximum. "
            "3. Sole Proprietorship — single owner, registered as a business name. "
            "4. Partnership — 2 to 20 partners. "
            "5. Branch of a Foreign Company — must register within 1 month of establishing "
            "a place of business in Tanzania. "
            "6. Trust, Society, and NGO registrations are also handled by BRELA."
        ),
        "keywords": ["type", "entity", "sole", "partnership", "limited", "company", "branch", "foreign", "ngo", "trust"],
    },

    {
        "topic": "Business Licence (BRELA) vs Trade Licence",
        "content": (
            "BRELA handles business registration (issuing a Certificate of Incorporation "
            "or Business Name Certificate). A separate Trade Licence is required from the "
            "relevant Local Government Authority (LGA) where the business operates. "
            "BRELA registration does not replace the Trade Licence requirement."
        ),
        "keywords": ["licence", "license", "trade", "lga", "local government", "permit"],
    },

    # ── TRA ──────────────────────────────────────────────────────────────────

    {
        "topic": "TIN Registration",
        "content": (
            "Every business entity in Tanzania must obtain a Taxpayer Identification Number "
            "(TIN) from TRA. TIN registration is free of charge and can be done online at "
            "https://www.tra.go.tz or at any TRA office. Required documents include: "
            "Certificate of Incorporation (or Business Name Certificate), Memorandum and "
            "Articles of Association, and national IDs of directors/owners. "
            "TIN must be obtained before commencing any taxable activity."
        ),
        "keywords": ["tin", "taxpayer", "identification", "number", "tax registration", "tra"],
    },

    {
        "topic": "VAT Registration Threshold",
        "content": (
            "VAT registration with TRA is mandatory when a business's annual taxable turnover "
            "reaches or is expected to reach TZS 200 million. Voluntary registration is allowed "
            "below this threshold. Once registered, businesses must charge VAT at the standard "
            "rate of 18% on taxable supplies, file monthly VAT returns by the last working day "
            "of the following month, and remit VAT collected to TRA."
        ),
        "keywords": ["vat", "value added tax", "threshold", "register", "200 million", "18%"],
    },

    {
        "topic": "Corporate Income Tax Rate",
        "content": (
            "The standard corporate income tax rate in Tanzania is 30% of net taxable profit. "
            "Newly listed companies on the Dar es Salaam Stock Exchange (DSE) enjoy a reduced "
            "rate of 25% for three years. Resident companies pay tax on worldwide income; "
            "non-resident companies pay tax only on Tanzania-source income. "
            "Tax returns must be filed within 6 months after the end of the accounting period."
        ),
        "keywords": ["corporate", "income tax", "rate", "30%", "profit", "tax return", "company tax"],
    },

    {
        "topic": "Pay As You Earn (PAYE)",
        "content": (
            "Employers in Tanzania are required to deduct PAYE from employee salaries and remit "
            "it to TRA by the 7th of the following month. The PAYE bands (2024/25) are: "
            "0 – 270,000 TZS/month: 0%. "
            "270,001 – 520,000: 8%. "
            "520,001 – 760,000: 20%. "
            "760,001 – 1,000,000: 25%. "
            "Above 1,000,000: 30%. "
            "Employers must also file a monthly PAYE return via the TRA online portal."
        ),
        "keywords": ["paye", "pay as you earn", "payroll", "salary", "employee", "employer", "deduction", "withholding"],
    },

    {
        "topic": "Skills and Development Levy (SDL)",
        "content": (
            "SDL is a levy imposed under Section 14 of the Vocational Education Training Act, Cap. 82, "
            "and collected by TRA. "
            "Who pays: Any employer with 10 or more employees must pay SDL. "
            "Rate: 3.5% of total gross emoluments paid to all employees during the month. "
            "Gross emoluments include: salaries, wages, payments in lieu of leave, fees, commissions, "
            "bonuses, gratuity, and allowances (subsistence, travel, entertainment, etc.). "
            "Employees covered: permanent, part-time, secondary, and casual labourers. "
            "Payment and filing: SDL is paid using form ITX 300.01.E and a monthly return must be "
            "submitted to TRA on or before the 7th of the following month. "
            "A half-year certificate reconciling monthly returns must also be prepared and remitted. "
            "Exempt from SDL: Government departments wholly financed by Government; Diplomatic Missions; "
            "UN and its organisations; international aid/technical assistance bodies; religious institutions "
            "whose employees solely administer worship, give religious instruction, or provide public health; "
            "charitable organisations; registered educational institutions (nursery to university); "
            "local government authorities; intern students under TESLA programme; "
            "farm employers whose employees are directly and solely engaged in farming."
        ),
        "keywords": [
            "sdl", "skills", "development", "levy", "payroll", "veta", "training",
            "3.5%", "emoluments", "itx 300", "10 employees",
        ],
    },

    {
        "topic": "Withholding Tax",
        "content": (
            "Tanzania imposes withholding tax on certain payments. Key rates: "
            "Dividends to residents: 5% (DSE-listed) / 10% (others). "
            "Dividends to non-residents: 10%. "
            "Interest to residents: 10%. Interest to non-residents: 10%. "
            "Royalties to residents: 15%. Royalties to non-residents: 15%. "
            "Service fees to non-residents: 15%. "
            "Rent (land/buildings): 10% for individuals, 10% for entities. "
            "The withholder must remit the tax to TRA by the 7th of the following month."
        ),
        "keywords": ["withholding", "wht", "dividend", "interest", "royalty", "rent", "non-resident"],
    },

    # ── STARTING A BUSINESS ───────────────────────────────────────────────────

    {
        "topic": "Starting a Business as an Individual — TIN & Business Licence Steps",
        "content": (
            "An individual (resident or non-resident) must first obtain a Taxpayer Identification Number (TIN) "
            "from TRA by visiting www.tra.go.tz. The Online TIN application form is available at "
            "https://taxpayerportal.tra.go.tz. Required identification: National ID, Passport, or Voter ID. "
            "For business TIN purposes, the individual must visit a TRA office with: "
            "(1) a letter from a local government leader, and "
            "(2) a lease agreement for the business location. "
            "Once the TIN certificate is issued, the taxpayer undergoes a tax assessment interview. "
            "After fulfilling tax obligations, a Tax Clearance Certificate is issued. "
            "This Tax Clearance is required to obtain a Business Licence from the Trade Office at "
            "the District, Municipal, or City level, or from the Ministry of Industry and Trade, "
            "depending on the type of business."
        ),
        "keywords": [
            "individual", "start", "starting", "sole", "tin", "business licence",
            "tax clearance", "resident", "non-resident", "trade office", "how to start",
        ],
    },

    {
        "topic": "Resident Individual — Definition for Tax Purposes",
        "content": (
            "An individual is considered a tax resident of Tanzania for a year of income if they: "
            "(1) Have a permanent home in Tanzania and are present in Tanzania during any part of the year; "
            "(2) Are present in Tanzania for periods totalling 183 days or more during the year of income; "
            "(3) Are present in Tanzania and in each of the two preceding years for periods averaging "
            "more than 122 days per year; or "
            "(4) Are an employee or official of the Government of Tanzania posted abroad during the year."
        ),
        "keywords": [
            "resident", "residency", "183 days", "122 days", "tax resident",
            "individual resident", "permanent home", "posted abroad",
        ],
    },

    {
        "topic": "Individual — Registering a Business Name with BRELA",
        "content": (
            "An individual may optionally register their business name with BRELA "
            "(Business Registration and Licensing Authority), an agency under the Ministry of Industry and Trade. "
            "The business name registration can be done before or after applying for a TIN. "
            "Once registered, the business name will appear on the TIN certificate alongside the "
            "individual's name in the format: '[Owner Name] trading as (T/A) [Business Name]'."
        ),
        "keywords": [
            "business name", "brela", "register name", "individual", "sole trader",
            "trading as", "t/a", "certificate of registration",
        ],
    },

    {
        "topic": "Starting a Business as a Limited Company (Corporation)",
        "content": (
            "To establish a limited company in Tanzania: "
            "Step 1 — Apply for a Certificate of Incorporation from BRELA. Directors must prepare "
            "a Memorandum and Articles of Association. "
            "Step 2 — Submit to BRELA: the Memorandum and Articles of Association, a lease agreement "
            "or title deed, and an introductory letter from the local authority. "
            "Step 3 — After BRELA registration, register on the TRA Taxpayer Portal, conduct a tax "
            "assessment, and submit returns for Income Tax, PAYE, and SDL. "
            "Step 4 — Upon meeting tax obligations, obtain a Tax Clearance Certificate. "
            "Step 5 — Use the Tax Clearance to obtain licences from other relevant business authorities."
        ),
        "keywords": [
            "company", "limited", "corporation", "incorporate", "incorporation",
            "certificate of incorporation", "directors", "memorandum", "articles of association",
            "start company", "register company",
        ],
    },

    {
        "topic": "Starting a Business as a Partnership",
        "content": (
            "To establish a partnership in Tanzania: "
            "Step 1 — Register the firm with BRELA and obtain a Certificate of Registration. "
            "Step 2 — Visit TRA with the partnership deed, which must state the names of all partners "
            "and their respective profit-sharing ratios. "
            "Step 3 — To apply for a TIN for the partnership, submit: the BRELA Certificate of "
            "Registration, the partnership deed, a lease agreement or title deed, and an introduction "
            "letter from the local authority. "
            "Step 4 — Each partner must individually apply for a personal TIN. If a partner already "
            "holds a TIN obtained for another purpose, that existing TIN must be used — a new application "
            "is not permitted."
        ),
        "keywords": [
            "partnership", "partners", "partner", "firm", "partnership deed",
            "profit sharing", "register partnership", "start partnership",
        ],
    },

    {
        "topic": "Starting a Business as a Trust",
        "content": (
            "A trust is a legal framework in which trustees manage assets separately from a partnership "
            "or corporation. To establish a trust for business purposes in Tanzania: "
            "Step 1 — Register with RITA (Registration, Insolvency and Trusteeship Agency) to obtain "
            "a Certificate of Registration. "
            "Step 2 — Create a trust deed listing the names and addresses of all trustees. "
            "Step 3 — Each trustee must apply for an individual TIN. If a trustee already holds a TIN "
            "obtained for another purpose, that existing TIN must be used — a new application is not permitted."
        ),
        "keywords": [
            "trust", "trustee", "trustees", "trust deed", "rita", "register trust",
            "start trust", "assets",
        ],
    },

    {
        "topic": "Registration of Aid Organisations",
        "content": (
            "An aid organisation is classified separately for tax purposes in Tanzania. "
            "The process is as follows: "
            "Step 1 — Obtain the necessary permit from the Ministry of Internal Affairs. "
            "Step 2 — Proceed with TIN registration via the TRA Taxpayer Portal, using the account "
            "of one of the organisation's authorised representatives."
        ),
        "keywords": [
            "aid", "aid organisation", "ngo", "ministry of internal affairs",
            "permit", "charitable", "organisation",
        ],
    },

    {
        "topic": "TIN Registration for Religious Institutions and Economic Groups",
        "content": (
            "Religious institutions and economic groups may apply for a TIN for tax purposes. "
            "Requirements: "
            "(1) A permit or introduction letter from their registered organisation, OR "
            "(2) A certificate of group registration from the District or Municipal authority. "
            "Registration is completed through the TRA Taxpayer Portal using the account of one "
            "of the group's authorised representatives."
        ),
        "keywords": [
            "religious", "church", "mosque", "institution", "economic group",
            "group registration", "district", "municipal", "tin", "permit",
        ],
    },

    # ── OBJECTIONS & APPEALS ─────────────────────────────────────────────────

    {
        "topic": "Tax Objections — Procedure and Requirements",
        "content": (
            "Governed by the Tax Administration Act No. 438 R.E 2023 and Tax Revenue Appeals Act, "
            "Cap. 408 R.E 2023. "
            "A taxpayer who believes the Commissioner General misapplied the law, reached an incorrect "
            "factual finding, abused his powers, was biased, or improperly considered or ignored evidence "
            "may object to the assessment. "
            "Procedure: File a written Notice of Objection to the Commissioner General within 30 days "
            "of the date the tax decision was served. The notice must state the grounds of objection and "
            "be accompanied by all relevant documents the taxpayer intends to rely on. "
            "Payment condition: The objection is not admitted unless the taxpayer has paid whichever "
            "is greater — the tax not in dispute OR one-third of the assessed tax. "
            "Waiver: A taxpayer may apply within 15 days of the tax decision for the Commissioner General "
            "to reduce or waive the required payment amount, if good reason exists. "
            "Suspension: Once a valid objection is filed and the statutory payment made, liability for "
            "the remaining assessed tax is suspended until the objection is finally determined. "
            "Extension of time: A taxpayer may apply for an extension within 7 days before the 30-day "
            "deadline. The extension granted shall not exceed 30 days. "
            "Where to lodge: Regional TRA office where the taxpayer is registered; Commissioner for "
            "Customs and Excise; Commissioner for Large Taxpayers; or Commissioner for Domestic Revenue."
        ),
        "keywords": [
            "objection", "object", "dispute", "assessment", "notice of objection",
            "30 days", "tax decision", "commissioner general", "tax administration act",
            "one third", "disputed", "waiver", "extension",
        ],
    },

    {
        "topic": "Tax Appeals — Board, Tribunal, and Court of Appeal",
        "content": (
            "There are three levels of appeal for tax disputes in Tanzania: "

            "1. Tax Revenue Appeals Board: "
            "Any person aggrieved by the Commissioner General's final determination may appeal to the Board. "
            "Conditions: (a) serve notice of appeal on the Commissioner General within 30 days of the "
            "final determination notice; (b) lodge the appeal with the Board within 45 days of the "
            "final determination notice; (c) the notice must include full details of the assessment and "
            "all correspondence with the Commissioner General. "

            "2. Tax Revenue Appeals Tribunal: "
            "Any party aggrieved by a Board decision may appeal to the Tribunal. "
            "Conditions: serve notice of intention to appeal on the opposite party within 15 days of "
            "the Board's decision; lodge the appeal within 30 days of the Board's decision. "

            "3. Court of Appeal: "
            "Any person aggrieved by a Tribunal decision may appeal to the Court of Appeal. "
            "Appeals to the Court of Appeal lie on questions of law only. "
            "The Appellate Jurisdiction Act and Court of Appeal Rules apply. "

            "Note: Any tax deposited as required during the objection/appeal process remains deposited "
            "with the Commissioner General pending the final determination of the appeal at all levels. "
            "The Board or Tribunal may extend time limits where the failure to appeal was caused by "
            "absence from Tanzania, sickness, or other reasonable cause."
        ),
        "keywords": [
            "appeal", "board", "tribunal", "court of appeal", "tax revenue appeals",
            "45 days", "30 days", "15 days", "aggrieved", "final determination",
            "tax revenue appeals act", "questions of law",
        ],
    },

    # ── EFD / VFD ─────────────────────────────────────────────────────────────

    {
        "topic": "Electronic Fiscal Devices (EFD) and Virtual Fiscal Devices (VFD) — Overview",
        "content": (
            "EFD (Electronic Fiscal Device): A physical receipt-issuing machine authorised by the "
            "Commissioner General for use in business transactions. "
            "VFD (Virtual Fiscal Device): A cloud-based software system approved by the Commissioner "
            "General to capture, transmit, and store sales data electronically. "
            "Both EFD and VFD serve the same purposes: improving business record quality, reducing "
            "tax evasion, ensuring fairness in tax assessment, minimising tax disputes, and enabling "
            "real-time monitoring of business transactions. "
            "Fiscal Receipt: A receipt or invoice issued using an EFD, the Government Electronic "
            "Payment Gateway, or any other electronic system approved by the Commissioner General."
        ),
        "keywords": [
            "efd", "vfd", "fiscal", "electronic fiscal device", "virtual fiscal device",
            "fiscal receipt", "receipt machine", "invoice", "pos",
        ],
    },

    {
        "topic": "EFD/VFD — Obligation to Acquire and Use",
        "content": (
            "Any person who supplies goods or renders services, or receives payment for goods or services, "
            "whose annual turnover is assessed at TZS 11 million or above, must acquire an EFD or VFD "
            "and issue fiscal receipts or fiscal invoices for all transactions. "
            "Rules for users: "
            "(1) EFD/VFD may be purchased from any TRA-approved supplier. "
            "(2) The device must not be transferred to any other person for any reason. "
            "(3) The device must be available, visible, and accessible at the business premises at all times. "
            "(4) If erroneous data is entered or the device fails for any reason, the user must report "
            "the incident to the approved supplier AND the Commissioner General within 24 hours."
        ),
        "keywords": [
            "efd", "vfd", "obligation", "acquire", "use", "11 million", "turnover",
            "fiscal receipt", "issue receipt", "approved supplier", "24 hours", "report",
        ],
    },

    {
        "topic": "EFD/VFD — Approved Supplier Requirements",
        "content": (
            "An EFD/VFD supplier must be certified by the Commissioner General. Responsibilities include: "
            "importing, distributing, and selling EFD/VFD devices; installing and configuring them; "
            "training users; and providing after-sales support including repairs and maintenance. "
            "Minimum requirements for approval as a supplier: "
            "Capital: TZS 1.5 billion for EFD suppliers; TZS 50 million for VFD suppliers. "
            "Technical team: Highly qualified staff to install, configure, train, and support users. "
            "Experience: Minimum 5 years supplying fiscal devices or similar ICT equipment. "
            "Any other requirements prescribed by the Commissioner General."
        ),
        "keywords": [
            "efd supplier", "vfd supplier", "approved supplier", "certified", "1.5 billion",
            "50 million", "capital requirement", "supplier", "install", "configure",
        ],
    },

    # ── DIGITAL / ELECTRONIC SERVICES TAXES ──────────────────────────────────

    {
        "topic": "Digital Service Tax (DST) — Income Tax on Electronic Services",
        "content": (
            "Under the Income Tax Act, Cap. 332: "
            "Section 89(m) establishes Tanzania as a source of income for payments made by individuals "
            "(not conducting business) to non-residents for services rendered. "
            "Section 90A requires non-resident persons to pay income tax at 2% on payments received "
            "from individuals not conducting business, for services rendered through a digital marketplace. "
            "Section 116(1) expands the scope to cover all electronic services, not only those via "
            "digital marketplaces. "
            "Section 116(2) sets the due date for DST return filing and payment as the 20th day of "
            "the following month. "
            "The DST rate is 2% of gross payments received. Input tax credit is not allowed. "
            "Non-resident providers are exempt from using Electronic Fiscal Devices (EFD)."
        ),
        "keywords": [
            "digital service tax", "dst", "electronic services", "non-resident", "digital marketplace",
            "section 89", "section 90a", "section 116", "2%", "income tax act",
        ],
    },

    {
        "topic": "VAT on Electronic Services — Non-Resident Providers",
        "content": (
            "Under the Value Added Tax Act, Cap. 148: "
            "Section 68(5) allows non-resident electronic service providers to register for VAT "
            "without requiring a tax representative in Tanzania. "
            "The VAT rate applicable is 18%. Input tax credit is not allowed. "
            "Returns and payment are due by the 20th day of the following month "
            "(per the VAT (Registration of Non-resident Electronic Service Providers) "
            "Amendment Regulations, 2023). "
            "Taxes must be paid to a designated bank account in Tanzanian Shillings or an equivalent "
            "convertible currency at the Bank of Tanzania's prevailing exchange rate on the date of payment. "
            "Non-resident providers are exempt from using Electronic Fiscal Devices (EFD)."
        ),
        "keywords": [
            "vat", "electronic services", "non-resident", "section 68", "vat act",
            "online services", "digital", "18%", "efd", "tax representative",
        ],
    },

    {
        "topic": "Registration for Non-Resident Electronic Service Providers (DST & VAT)",
        "content": (
            "The Income Tax (Registration of Non-resident Electronic Service Providers/Suppliers) "
            "Regulations, 2022 and the VAT (Registration of Non-resident Electronic Service "
            "Providers/Suppliers) Regulations, 2022 govern registration. "
            "Regulation 4 of both sets of regulations requires eligible non-resident electronic "
            "service providers or suppliers to apply online through the Commissioner General's "
            "Simplified Online Registration Portal. "
            "There is NO registration threshold — all qualifying non-residents must register "
            "regardless of turnover. "
            "Filing and payment of both DST and VAT returns must be done electronically."
        ),
        "keywords": [
            "register", "non-resident", "electronic service", "registration portal",
            "regulation 4", "simplified", "threshold", "dst", "vat", "2022 regulations",
        ],
    },

    {
        "topic": "Withholding Tax on Digital Content Creators and Digital Assets",
        "content": (
            "Introduced by the Finance Act, 2024 under the Income Tax Act, Cap. 332: "
            "Section 83B: Any resident or non-resident making payments to resident digital content "
            "creators must withhold tax at 5% on such payments. "
            "Section 83C: Any resident or non-resident owning or facilitating a digital asset "
            "exchange platform must withhold tax at 3% on payments made to resident persons for "
            "the exchange or transfer of digital assets. "
            "Additionally, the Finance Act, 2024 introduced a new definition of 'Online Data Services' "
            "under Section 2 of the VAT Act, Cap. 148."
        ),
        "keywords": [
            "digital content", "content creator", "digital asset", "crypto", "exchange",
            "section 83b", "section 83c", "5%", "3%", "finance act 2024", "withholding",
            "online data services",
        ],
    },

    # ── STAMP DUTY ────────────────────────────────────────────────────────────

    {
        "topic": "Stamp Duty — Introduction and Scope",
        "content": (
            "The Stamp Duty Act consolidates and revises laws on stamp duty in Tanzania Mainland. "
            "Any instrument specified in the schedule that is: "
            "(a) executed in Tanzania Mainland, OR "
            "(b) executed outside Tanzania Mainland but relates to property or a matter performed in Tanzania Mainland, "
            "must be charged with stamp duty at the amount specified in the schedule, unless exempted. "
            "Stamp duty is generally payable by the person drawing, making, or executing the instrument. "
            "If a person is uncertain whether an instrument requires stamping or what amount is due, "
            "they may refer the matter to the Stamp Duty Officer for adjudication."
        ),
        "keywords": [
            "stamp duty", "instrument", "stamp", "adjudication", "stamp duty act",
            "executed", "chargeable",
        ],
    },

    {
        "topic": "Stamp Duty — Time Limit for Stamping",
        "content": (
            "All chargeable instruments executed in Tanzania Mainland must be stamped within 30 days "
            "of execution. "
            "If the instrument is presented to a proper officer for adjudication, the period from "
            "presentation until notification of the officer's decision is excluded from the 30-day count. "
            "Receipts, acknowledgements of debt, promissory notes, and bills of exchange must be "
            "stamped on the date of execution or the date shown on the instrument."
        ),
        "keywords": [
            "stamp duty", "30 days", "time limit", "stamped", "adjudication",
            "promissory note", "bill of exchange", "receipt",
        ],
    },

    {
        "topic": "Stamp Duty — Rates on Common Instruments",
        "content": (
            "Stamp duty rates on common instruments in Tanzania Mainland: "
            "Affidavit (including affirmation or declaration): TZS 2,000. "
            "Agreement or Memorandum of Agreement: TZS 2,000. "
            "Agreement relating to Deposit of Title Deeds, Hypothecation, Pawn or Pledge: TZS 2,000. "
            "Appraisement or Valuation (not under court order): TZS 500. "
            "Exchange of Property: 0.5% on the first TZS 100,000, then 1% on the value exceeding TZS 100,000. "
            "Lease (including sub-lease or agreement to let): 1% of the annual reserved rent, for all durations. "
            "Memorandum of Association of a Company: TZS 10,000. "
            "Instrument of Partnership — capital up to TZS 10,000: TZS 1,000; "
            "capital TZS 100,001–1,000,000: TZS 5,000; any other case: TZS 10,000; "
            "Dissolution of partnership: TZS 10,000. "
            "Power of Attorney: TZS 2,000. "
            "Transfer of shares in an incorporated company: 1% of the board-approved value. "
            "Transfer of debentures: 1% of the board-approved value. "
            "Transfer of interest secured by bond, mortgage-deed, or policy of insurance: 1% of value."
        ),
        "keywords": [
            "stamp duty", "rate", "affidavit", "agreement", "lease", "memorandum",
            "partnership", "power of attorney", "transfer", "shares", "debenture",
            "mortgage", "property", "instrument", "tshs", "duty rate",
        ],
    },

]


def search(question: str) -> list[dict]:
    """Return knowledge base entries whose keywords appear in the question."""
    q = question.lower()
    matched = []
    for entry in ENTRIES:
        if any(kw.lower() in q for kw in entry["keywords"]):
            matched.append(entry)
    return matched


def format_entries(entries: list[dict]) -> str:
    """Format matched entries as context text."""
    if not entries:
        return ""
    parts = []
    for e in entries:
        parts.append(f"[Knowledge Base — {e['topic']}]\n{e['content']}")
    return "\n\n---\n\n".join(parts)

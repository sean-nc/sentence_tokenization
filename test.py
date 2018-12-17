from tokenizer import paragraph_to_sentences

paragraphs = [
  "Job Summary: First Quadrant in Pasadena seeks an Equity Research Analyst. Will independently research, analyze and model quantitative research topics relevant to stock selection and portfolio mgmt; perform statistical/economic research; translate fundamental ideas into investment models; interpret and present research results; provide other research and support as needed. Requirements include: Advanced degree in finance, economics, or data science; familiarity with time series analysis, factor analysis, machine learning; knowledge of Python/Pandas.",
  "We are focused on identifying fundamental inflection points to aid in the rigorous analysis of our covered companies and industry forecasts. Our clients find value from getting in front of key themes and trends that lead to better strategic and financial decisions. We are committed to a singular focus on providing the most accurate and reliable research product in the market. If you are interested in equity and market research within an environment that fosters teamwork and excellence, Cleveland Research could be the place for you!",
  "Cleveland Research Company is an employee owned, independent research firm, headquartered in Cleveland, Ohio. Founded in 2006, CRC has expanded to 15 research teams publishing research on over 150 companies. We pride ourselves on a disciplined research process that has us regularly engaged with the industries and companies we cover.",
  "EOE Policy Statement : American Century Investments believes all individuals are entitled to equal employment opportunity and advancement opportunities without regard to race, religious creed, color, sex, national origin, ancestry, physical disability, mental disability, medical condition, genetic information, marital status, gender, gender identity, gender expression, age for individuals forty years of age and older, military and veteran status, sexual orientation, and any other basis protected by applicable federal, state and local laws. ACI does not discriminate or adopt any policy that discriminates against an individual or any group of individuals on any of these bases.",
  "Voya Investment Management (Voya IM) is a leading active asset management firm. As of September 30, 2018, Voya IM manages approximately $223 billion for affiliated and external institutions as well as individual investors. Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  "The analyst will work with the Senior Analyst to develop and communicate investment recommendations based on comprehensive industry and company research, relying on various sources of information including, but not limited to, review of public documents, annual reports, trade journals, networking with industry contacts and interaction with senior management teams within the sector. The analyst will be highly proficient in modeling and engaging with data more broadly and will be expected to effectively communicate both in written and oral formats with portfolio managers.",
  "Voya Investment Management (Voya IM) is a leading active asset management firm. As of March 31, 2018, Voya IM manages approximately $227 billion* for affiliated and external institutions as well as individual investors. Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  "All qualified applicants will receive consideration for employment and will not be discriminated against on the basis of race, colour, religion, sex, sexual orientation, national origin, age, disability, protected veteran status, genetic information, marital status, gender identity or any other impermissible criterion or circumstance. Macquarie also takes affirmative action in support of its policy to hire and advance in employment of individuals who are minorities, women, protected veterans, and individuals with disabilities",
  "Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment management and wealth management services. The Firm's employees serve clients worldwide including corporations, governments and individuals from more than 1,200 offices in 43 countries. As a market leader, the talent and passion of our people is critical to our success. Together, we share a common set of values rooted in integrity, excellence and strong team ethic. Morgan Stanley can provide a superior foundation for building a professional career - a place for people to learn, to achieve and grow. A philosophy that balances personal lifestyles, perspectives and needs is an important part of our culture.ResearchMorgan Stanley Investment Research is uniquely committed to being an essential part of our clients' investment process. We strive to be the sell-side research provider that best understands the buy side. Through relevant and timely conversations with leading investors, we focus resources on risk-reward essentials: identifying the investor debates, assessing the potential outcomes, and uncovering the evidence our clients need to validate their investment decisions. Our equity analysts cover some 2,900 stocks; our economists, strategists and fixed income analysts cover all major regions and other asset classes around the globe.Equity Research The Equity Research department is responsible for researching macroeconomic and microeconomic conditions, along with company fundamentals. It also collects and analyzes financial information to make investment recommendations on stocks in specific sectors. Research analysts build financial models to explore alternative scenarios, examine industries and communicate with companies and investors. Equity Research team members discuss their analysis and investment recommendations in research notes. A career in investment research at Morgan Stanley demands a commitment to excellence and a passion for the markets as well as the highest level of integrity.We are seeking an Analyst/Associate to join our Payments team in New York, NY.",
  "Skills Required• The candidate will have prior professional experience in Equity Research, Consulting, Investment Banking/M&A/Capital Markets and/or Accounting• Sector experience is a plus• Experience utilizing Excel for: Building/Maintaining Financial models - advanced level of excel proficiency is expected and required• Writing experience in a professional capacity – i.e.: Crafting Equity Research notes/correspondence; presentation or development of industry report• Candidates are expected to be adaptable and have the ability to work well under pressure• Strong PowerPoint skills are required• CFA is a plus",
  "This position has responsibility for setting the research agenda for quantitative equity, including thought leadership in quantitative research, investment ideas, and portfolio design for Voya Investment Management (Voya IM). With a strong background in technical computing and statistics, you will be responsible for accelerating the development and design of new quantitative research and strategies. This will include empirical research into U.S. and global equity market inefficiencies. Must be familiar with fundamental, expectational and market data, have a solid knowledge of asset pricing literature, and strong programming skills. The individual will represent the views of the team across the firm and to the industry at large.",
  "Voya Investment Management (Voya IM) is a leading active asset management firm. As of March 31, 2018, Voya IM manages approximately $227 billion* for affiliated and external institutions as well as individual investors. Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  "Credit Suisse is an equal opportunity employer. Welcoming diversity gives us a competitive advantage in the global marketplace and drives our success. Credit Suisse complies with applicable federal, state, and local laws prohibiting discrimination in employment in every jurisdiction in which it maintains facilities. Subject to applicable law and regulatory requirements, Credit Suisse complies with state and local laws regarding considering for employment qualified individuals with criminal histories.",
  "Credit Suisse is a leading global wealth manager with strong investment banking capabilities. Founded in 1856 to pioneer the country’s railways and economic expansion, Credit Suisse has expanded to be a global force employing over 48,000 people in 50 countries. With new leadership, a new strategy, and a streamlined global organization, we serve our clients through five divisions: our Swiss Universal Bank; International Wealth Management; Asia Pacific; Global Markets; and Investment Banking and Capital Markets. These divisions are supported by our Corporate functions, including technology, operations, risk management, compliance, and more. We partner across businesses and regions to create innovative solutions to meet the needs of our clients and to help our employees grow. We will invest in your development with ongoing opportunities for training, networking, and mobility. Join us and let's shape the new Credit Suisse together.",
  "At Credit Suisse, the Supervisory Analyst has an integral role in ensuring the Equity Research department is fully compliant with all regulatory and compliance rules and policies. You will gain excellent exposure in a critical and highly valued role of Credit Suisse's premiere business franchise. Through your leadership, experience, and knowledge of FINRA rules and regulations, you will work with the Supervisory Analyst team and with research management to maintain policy and controls. Our Research Department is one of the top rated on Wall Street and our partners on the global Supervisory Analyst team are highly experienced and motivated.",
  "Goldman Sachs Asset Management (GSAM) delivers innovative investment solutions through a global, multi-product platform that offers clients the advantages that come with working with a large firm, while maintaining the benefits of a boutique. GSAM is one of the pre-eminent investment management organizations globally. Critical to the success of GSAM is our ability to leverage a global team of talented professionals to define solutions and lead change across the operational infrastructure. Goldman Sachs Asset Management is looking for a research analyst to join the US Small Cap Value Fundamental Equity team. The Goldman Sachs US Small Cap Value team invests in small cap long-only U.S. equity strategies in a classic value approach with a quality bias. Our bottom-up investment process to investing focuses on quality businesses that sell at a discount to our assessment of the business fair value. Our core strength is in stock picking, we seek to generate the majority of our alpha through security selection, rather than other means such as sector rotation or market timing. We maintain a long-term investment horizon.",
  "The analyst will be responsible for executing the investment research process. Responsibilities include building and maintaining financial models, conducting valuation analysis (comps, DCF, IRR, Merger models, private market value), writing investment briefs and presentations, conducting company/industry due diligence, meeting with management teams and industry participants in office and at industry conferences.",
  "We’re a team of trusted advisors who provide innovative investment solutions to help our clients meet their financial goals. From private wealth to asset management, we work with specialists and groups from around the firm to help high-net-worth individuals and institutions across various industries navigate changing markets and make smart investments. We value self-starters with an entrepreneurial spirit, but still provide the support and resources to ensure your success.",
  "Diversity is a key business imperative and a source of strength at Citi. We serve clients from every walk of life, every background and every origin. Our goal is to have our workforce reflect this same diversity at all levels. Citi has made it a priority to foster a culture where the best people want to work, where individuals are promoted based on merit, where we value and demand respect for others and where opportunities to develop are widely available to all.",
  "Citi’s Mission and Value Proposition explains what we do and Citi Leadership Standards explain how we do it. Our mission is to serve as a trusted partner to our clients by responsibly providing financial services that enable growth and economic progress. We strive to earn and maintain our clients’ and the public’s trust by constantly adhering to the highest ethical standards and making a positive impact on the communities we serve. Our Leadership Standards is a common set of skills and expected behaviors that illustrate how our employees should work every day to be successful and strengthens our ability to execute against our strategic priorities.",
  "Citi, the leading global bank, has approximately 200 million customer accounts and does business in more than 160 countries and jurisdictions. Citi provides consumers, corporations, governments and institutions with a broad range of financial products and services, including consumer banking and credit, corporate and investment banking, securities brokerage, transaction services, and wealth management. Our core activities are safeguarding assets, lending money, making payments and accessing the capital markets on behalf of our clients.",
  "NYC-based equity research job covering: Medical Devices or Life Sciences. This is an opportunity to work with a highly regarded advisory, banking and research boutique as a Sr Analyst on an expanding equity research team. The Sr Analyst and will be responsible for : research, valuations, written notes/reports, communicating with clients and sales/traders, and participating in investment banking. Strong writing, modeling, excel and power point skills required.",
  "The Active Quantitative Equity (AQE) team manages approximately $35 billion in a range of strategies across global equity markets over a broad active risk spectrum. We are active managers, focused on solving investment problems. Built by a team with decades of experience, the stock-selection model that informs all of our solutions contain our best investment insights — carefully scrutinized, extensively tested and grounded in a strong economic rationale. Quantitative research that combines creative investment insights with rigorous statistical testing is an integral part of AQE’s investment process.",
  "Assisting in the preparation of company and industry research reports (e.g. quarterly reporting initiatives and marketing packages)",
  "Are you reading this and getting excited about contributing to our research and bringing our insights to life? Connect with us now to be a part of our enthusiastic, dynamic and entrepreneurial team! Email your cover letter and resume to hr @hotspex.comand start writing your own compelling career story.",
  "Reporting to the Principal Investigator, the Research Officer will provide research support for the Public Health Training for Equitable Systems Change project. The Public Health Training for Equitable Systems Change (PHESC), is a collaboration between the Dalla Lana School of Public Health (DLSPH), the Alliance for Healthier Communities, National Collaborating Centre for Methods and Tools, National Collaborating Centre for Determinants of Health, Ontario Public Health Association, Public Health Ontario, Wellesley Institute, and the National Collaborating Centre for Healthy Public Policy. The purpose of this two-year grant is to support the development, implementation and evaluation of a comprehensive training plan to improve knowledge, skills, and performance of Ontario’s public health workforce while integrating a health equity approach. PHESC is funded by the Ontario Ministry of Health and Long-Term Care through the Health and Well-Being Grant.",
  "Fostering positive relationships with project partners; communicating project progress to public health stakeholders; reviewing and summarizing research literature; formatting collected data for presentations and reports; coordinating meeting schedules; keeping well-informed on current training resources and practices; preparing and editing documents; collecting data; preparing draft evaluation reports and summaries of collected data; analyzing results and preparing reports for research papers and other knowledge products.",
  "Employee Group: United Steelworkers (USW)",
  "Pay Scale Group and Hiring Rate: USW Pay Band 08 - $52,996 with an annual step progression to a maximum of $67,774. Pay scale and job class assignment is subject to determination pursuant to the Job Evaluation/Pay Equity Maintenance Protocol."
]

expected_paragraphs = [
  [
    "Job Summary: First Quadrant in Pasadena seeks an Equity Research Analyst.",
    "Will independently research, analyze and model quantitative research topics relevant to stock selection and portfolio mgmt; perform statistical/economic research; translate fundamental ideas into investment models; interpret and present research results; provide other research and support as needed.",
    "Requirements include: Advanced degree in finance, economics, or data science; familiarity with time series analysis, factor analysis, machine learning; knowledge of Python/Pandas."
  ],
  [
    "We are focused on identifying fundamental inflection points to aid in the rigorous analysis of our covered companies and industry forecasts.",
    "Our clients find value from getting in front of key themes and trends that lead to better strategic and financial decisions.",
    "We are committed to a singular focus on providing the most accurate and reliable research product in the market."
    "If you are interested in equity and market research within an environment that fosters teamwork and excellence, Cleveland Research could be the place for you!"
  ],
  [
    "Cleveland Research Company is an employee owned, independent research firm, headquartered in Cleveland, Ohio.",
    "Founded in 2006, CRC has expanded to 15 research teams publishing research on over 150 companies.",
    "We pride ourselves on a disciplined research process that has us regularly engaged with the industries and companies we cover."
  ],
  [
    "EOE Policy Statement : American Century Investments believes all individuals are entitled to equal employment opportunity and advancement opportunities without regard to race, religious creed, color, sex, national origin, ancestry, physical disability, mental disability, medical condition, genetic information, marital status, gender, gender identity, gender expression, age for individuals forty years of age and older, military and veteran status, sexual orientation, and any other basis protected by applicable federal, state and local laws.",
    "ACI does not discriminate or adopt any policy that discriminates against an individual or any group of individuals on any of these bases.",
  ],
  [
    "Voya Investment Management (Voya IM) is a leading active asset management firm.",
    "As of September 30, 2018, Voya IM manages approximately $223 billion for affiliated and external institutions as well as individual investors.",
    "Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  ],
  [
    "The analyst will work with the Senior Analyst to develop and communicate investment recommendations based on comprehensive industry and company research, relying on various sources of information including, but not limited to, review of public documents, annual reports, trade journals, networking with industry contacts and interaction with senior management teams within the sector.",
    "The analyst will be highly proficient in modeling and engaging with data more broadly and will be expected to effectively communicate both in written and oral formats with portfolio managers.",
  ],
  [
    "Voya Investment Management (Voya IM) is a leading active asset management firm.",
    "As of March 31, 2018, Voya IM manages approximately $227 billion* for affiliated and external institutions as well as individual investors.",
    "Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  ],
  [
    "All qualified applicants will receive consideration for employment and will not be discriminated against on the basis of race, colour, religion, sex, sexual orientation, national origin, age, disability, protected veteran status, genetic information, marital status, gender identity or any other impermissible criterion or circumstance.",
    "Macquarie also takes affirmative action in support of its policy to hire and advance in employment of individuals who are minorities, women, protected veterans, and individuals with disabilities",
  ],
  [
    "Morgan Stanley is a leading global financial services firm providing a wide range of investment banking, securities, investment management and wealth management services.",
    "The Firm's employees serve clients worldwide including corporations, governments and individuals from more than 1,200 offices in 43 countries.",
    "As a market leader, the talent and passion of our people is critical to our success.",
    "Together, we share a common set of values rooted in integrity, excellence and strong team ethic.",
    "Morgan Stanley can provide a superior foundation for building a professional career - a place for people to learn, to achieve and grow.",
    "A philosophy that balances personal lifestyles, perspectives and needs is an important part of our culture.",
    "ResearchMorgan Stanley Investment Research is uniquely committed to being an essential part of our clients' investment process.",
    "We strive to be the sell-side research provider that best understands the buy side.",
    "Through relevant and timely conversations with leading investors, we focus resources on risk-reward essentials: identifying the investor debates, assessing the potential outcomes, and uncovering the evidence our clients need to validate their investment decisions.",
    "Our equity analysts cover some 2,900 stocks; our economists, strategists and fixed income analysts cover all major regions and other asset classes around the globe.",
    "Equity Research The Equity Research department is responsible for researching macroeconomic and microeconomic conditions, along with company fundamentals.",
    "It also collects and analyzes financial information to make investment recommendations on stocks in specific sectors.",
    "Research analysts build financial models to explore alternative scenarios, examine industries and communicate with companies and investors.",
    "Equity Research team members discuss their analysis and investment recommendations in research notes.",
    "A career in investment research at Morgan Stanley demands a commitment to excellence and a passion for the markets as well as the highest level of integrity.",
    "We are seeking an Analyst/Associate to join our Payments team in New York, NY.",
  ],
  [
    "Skills Required",
    "• The candidate will have prior professional experience in Equity Research, Consulting, Investment Banking/M&A/Capital Markets and/or Accounting",
    "• Sector experience is a plus",
    "• Experience utilizing Excel for: Building/Maintaining Financial models - advanced level of excel proficiency is expected and required",
    "• Writing experience in a professional capacity – i.e.: Crafting Equity Research notes/correspondence; presentation or development of industry report",
    "• Candidates are expected to be adaptable and have the ability to work well under pressure",
    "• Strong PowerPoint skills are required",
    "• CFA is a plus",
  ],
  [
    "This position has responsibility for setting the research agenda for quantitative equity, including thought leadership in quantitative research, investment ideas, and portfolio design for Voya Investment Management (Voya IM).",
    "With a strong background in technical computing and statistics, you will be responsible for accelerating the development and design of new quantitative research and strategies.",
    "This will include empirical research into U.S. and global equity market inefficiencies.",
    "Must be familiar with fundamental, expectational and market data, have a solid knowledge of asset pricing literature, and strong programming skills.",
    "The individual will represent the views of the team across the firm and to the industry at large.",
  ],
  [
    "Voya Investment Management (Voya IM) is a leading active asset management firm.",
    "As of March 31, 2018, Voya IM manages approximately $227 billion* for affiliated and external institutions as well as individual investors.",
    "Drawing on over 40 years of experience and an ongoing commitment to reliable investing, Voya IM has the resources and expertise to help long-term investors achieve strong investment results.",
  ],
  [
    "Credit Suisse is an equal opportunity employer.",
    "Welcoming diversity gives us a competitive advantage in the global marketplace and drives our success.",
    "Credit Suisse complies with applicable federal, state, and local laws prohibiting discrimination in employment in every jurisdiction in which it maintains facilities.",
    "Subject to applicable law and regulatory requirements, Credit Suisse complies with state and local laws regarding considering for employment qualified individuals with criminal histories.",
  ],
  [
    "Credit Suisse is a leading global wealth manager with strong investment banking capabilities.",
    "Founded in 1856 to pioneer the country’s railways and economic expansion, Credit Suisse has expanded to be a global force employing over 48,000 people in 50 countries.",
    "With new leadership, a new strategy, and a streamlined global organization, we serve our clients through five divisions: our Swiss Universal Bank; International Wealth Management; Asia Pacific; Global Markets; and Investment Banking and Capital Markets.",
    "These divisions are supported by our Corporate functions, including technology, operations, risk management, compliance, and more.",
    "We partner across businesses and regions to create innovative solutions to meet the needs of our clients and to help our employees grow.",
    "We will invest in your development with ongoing opportunities for training, networking, and mobility.",
    "Join us and let's shape the new Credit Suisse together.",
  ],
  [
    "At Credit Suisse, the Supervisory Analyst has an integral role in ensuring the Equity Research department is fully compliant with all regulatory and compliance rules and policies.",
    "You will gain excellent exposure in a critical and highly valued role of Credit Suisse's premiere business franchise.",
    "Through your leadership, experience, and knowledge of FINRA rules and regulations, you will work with the Supervisory Analyst team and with research management to maintain policy and controls.",
    "Our Research Department is one of the top rated on Wall Street and our partners on the global Supervisory Analyst team are highly experienced and motivated.",
  ],
  [
    "Goldman Sachs Asset Management (GSAM) delivers innovative investment solutions through a global, multi-product platform that offers clients the advantages that come with working with a large firm, while maintaining the benefits of a boutique.",
    "GSAM is one of the pre-eminent investment management organizations globally.",
    "Critical to the success of GSAM is our ability to leverage a global team of talented professionals to define solutions and lead change across the operational infrastructure.",
    "Goldman Sachs Asset Management is looking for a research analyst to join the US Small Cap Value Fundamental Equity team.",
    "The Goldman Sachs US Small Cap Value team invests in small cap long-only U.S. equity strategies in a classic value approach with a quality bias.",
    "Our bottom-up investment process to investing focuses on quality businesses that sell at a discount to our assessment of the business fair value.",
    "Our core strength is in stock picking, we seek to generate the majority of our alpha through security selection, rather than other means such as sector rotation or market timing.",
    "We maintain a long-term investment horizon.",
  ],
  [
    "The analyst will be responsible for executing the investment research process.",
    "Responsibilities include building and maintaining financial models, conducting valuation analysis (comps, DCF, IRR, Merger models, private market value), writing investment briefs and presentations, conducting company/industry due diligence, meeting with management teams and industry participants in office and at industry conferences.",
  ],
  [
    "We’re a team of trusted advisors who provide innovative investment solutions to help our clients meet their financial goals.",
    "From private wealth to asset management, we work with specialists and groups from around the firm to help high-net-worth individuals and institutions across various industries navigate changing markets and make smart investments.",
    "We value self-starters with an entrepreneurial spirit, but still provide the support and resources to ensure your success.",
  ],
  [
    "Diversity is a key business imperative and a source of strength at Citi.",
    "We serve clients from every walk of life, every background and every origin.",
    "Our goal is to have our workforce reflect this same diversity at all levels.",
    "Citi has made it a priority to foster a culture where the best people want to work, where individuals are promoted based on merit, where we value and demand respect for others and where opportunities to develop are widely available to all.",
  ],
  [
    "Citi’s Mission and Value Proposition explains what we do and Citi Leadership Standards explain how we do it.",
    "Our mission is to serve as a trusted partner to our clients by responsibly providing financial services that enable growth and economic progress.",
    "We strive to earn and maintain our clients’ and the public’s trust by constantly adhering to the highest ethical standards and making a positive impact on the communities we serve.",
    "Our Leadership Standards is a common set of skills and expected behaviors that illustrate how our employees should work every day to be successful and strengthens our ability to execute against our strategic priorities.",
  ],
  [
    "Citi, the leading global bank, has approximately 200 million customer accounts and does business in more than 160 countries and jurisdictions.",
    "Citi provides consumers, corporations, governments and institutions with a broad range of financial products and services, including consumer banking and credit, corporate and investment banking, securities brokerage, transaction services, and wealth management.",
    "Our core activities are safeguarding assets, lending money, making payments and accessing the capital markets on behalf of our clients.",
  ],
  [
    "NYC-based equity research job covering: Medical Devices or Life Sciences.",
    "This is an opportunity to work with a highly regarded advisory, banking and research boutique as a Sr Analyst on an expanding equity research team.",
    "The Sr Analyst and will be responsible for : research, valuations, written notes/reports, communicating with clients and sales/traders, and participating in investment banking.",
    "Strong writing, modeling, excel and power point skills required.",
  ],
  [
    "The Active Quantitative Equity (AQE) team manages approximately $35 billion in a range of strategies across global equity markets over a broad active risk spectrum.",
    "We are active managers, focused on solving investment problems.",
    "Built by a team with decades of experience, the stock-selection model that informs all of our solutions contain our best investment insights — carefully scrutinized, extensively tested and grounded in a strong economic rationale.",
    "Quantitative research that combines creative investment insights with rigorous statistical testing is an integral part of AQE’s investment process.",
  ],
  [
    "Assisting in the preparation of company and industry research reports (e.g. quarterly reporting initiatives and marketing packages)",
  ],
  [
    "Are you reading this and getting excited about contributing to our research and bringing our insights to life?",
    "Connect with us now to be a part of our enthusiastic, dynamic and entrepreneurial team!",
    "Email your cover letter and resume to hr @hotspex.comand start writing your own compelling career story.",
  ],
  [
    "Reporting to the Principal Investigator, the Research Officer will provide research support for the Public Health Training for Equitable Systems Change project.",
    "The Public Health Training for Equitable Systems Change (PHESC), is a collaboration between the Dalla Lana School of Public Health (DLSPH), the Alliance for Healthier Communities, National Collaborating Centre for Methods and Tools, National Collaborating Centre for Determinants of Health, Ontario Public Health Association, Public Health Ontario, Wellesley Institute, and the National Collaborating Centre for Healthy Public Policy.",
    "The purpose of this two-year grant is to support the development, implementation and evaluation of a comprehensive training plan to improve knowledge, skills, and performance of Ontario’s public health workforce while integrating a health equity approach.",
    "PHESC is funded by the Ontario Ministry of Health and Long-Term Care through the Health and Well-Being Grant.",
  ],
  [
    "Fostering positive relationships with project partners; communicating project progress to public health stakeholders; reviewing and summarizing research literature; formatting collected data for presentations and reports; coordinating meeting schedules; keeping well-informed on current training resources and practices; preparing and editing documents; collecting data; preparing draft evaluation reports and summaries of collected data; analyzing results and preparing reports for research papers and other knowledge products.",
  ],
  [
    "Employee Group: United Steelworkers (USW)",
  ],
  [
    "Pay Scale Group and Hiring Rate: USW Pay Band 08 - $52,996 with an annual step progression to a maximum of $67,774.",
    "Pay scale and job class assignment is subject to determination pursuant to the Job Evaluation/Pay Equity Maintenance Protocol."
  ],
]

count = 0
for index, paragraph in enumerate(paragraphs):
  paragraph = paragraph_to_sentences(paragraph)
  if paragraph == expected_paragraphs[index]:
    count += 1
  else:
    print("\n=============")
    print("Function:")
    for sentence in paragraph:
      print("\n", sentence)
    print("\n=============")
    print("\ndoesn't equal\n")
    print("=============\n")
    print("Expected:")
    for sentence in expected_paragraphs[index]:
      print("\n", sentence)
    print("=============\n")


print("{} out of {} passed.".format(count, len(paragraphs)))
print("{}%".format(int((count / len(paragraphs))*100)))

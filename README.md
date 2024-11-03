# ClimateChange

# Abstract
 — This project aims to develop an innovative climate resilience data platform that integrates predictive modeling and time-series analysis. Unlike traditional systems offering static data visualization, this solution is designed to evolve, incorporating dynamic, real-time data processing capabilities in future iterations to enhance the accuracy and timeliness of environmental risk assessments. Using Python for data processing and NoSQL databases for managing unstructured data, the platform currently analyzes multiple data types, such as historical weather, vegetation patterns, and demographic factors, to deliver comprehensive risk assessments. A central feature is the Wildfire Risk Prediction Dashboard, developed to forecast wildfire occurrences across Canadian forests by correlating historical climate events with updated weather and vegetation data. The platform also extends its capabilities to cover other critical climate hazards, including heatwaves and floods, offering a holistic view of climate risks. By structuring the system to accommodate real-time updates through scalable architecture, the platform represents a significant advancement in climate resilience, providing actionable insights for governments and organizations to support proactive disaster risk reduction efforts.

# Introduction

Climate change is significantly intensifying the frequency and severity of natural disasters worldwide. In Canada, the impact is particularly severe, with the country warming at nearly twice the global average [1]. This rapid warming has contributed to an increase in extreme weather events, including record-breaking wildfires, floods, and heatwaves, threatening ecosystems, communities, and economies. For instance, in 2023 [2], Canada experienced its worst wildfire season on record, burning over 17 million hectares of forest, leading to the evacuation of thousands of residents and severely impacting air quality across North America. The situation continued in 2024 [3], with the Jasper, Alberta wildfires causing extensive damage to ecosystems and disrupting local communities and industries reliant on tourism. These events highlight the urgent need for advanced tools that enhance climate resilience and disaster preparedness. To address these challenges, Eco-Trend Architects are developing an advanced data platform that integrates predictive modeling, geospatial analysis, and time-series data to better forecast and manage climate hazards specific to Canada.

 # A.	Project Aim
The aim of this project is to build a comprehensive data platform designed to improve climate resilience by providing reliable, data-driven risk assessments. The platform will offer governments and organizations the tools needed to predict, analyze, and respond proactively to climate hazards, such as wildfires, floods, and heatwaves, to strengthen disaster preparedness and minimize impacts.

# B.	Project Objectives 
The project focuses on several key objectives to achieve this aim. The platform will develop a Wildfire Risk Prediction Dashboard, which leverages historical weather patterns, vegetation data, and records of human activities that contribute to carbon emissions to forecast wildfire risks across Canadian forests. By analyzing these variables, the dashboard will provide targeted insights into high-risk areas, allowing for timely preventive measures. Additionally, the platform integrates NoSQL databases, such as MongoDB, for managing unstructured environmental data. 
This approach ensures efficient handling of the vast and diverse datasets required for accurate risk analysis. Geospatial analysis capabilities are embedded in the system through PostgreSQL/MongoDB, enabling precise monitoring of environmental variables. For instance, the platform will track temperature trends, soil moisture levels, and vegetation density to predict the probability and intensity of wildfire outbreaks. This technology is further supported by cloud-based solutions and APIs, ensuring the platform is scalable and adaptable, capable of integrating data from climate monitoring agencies like Environment and Climate Change Canada.
Beyond wildfire risks, the platform offers a comprehensive overview of other climate hazards. For example, it incorporates data on floods such as the severe flooding that devastated British Columbia in 2021, causing billions in damages and displacing thousands as well as heatwaves, which have become increasingly frequent in Canadian cities, leading to health risks and infrastructure strain. By providing insights into multiple hazards, the platform offers a holistic view of the environmental risks facing Canadian communities. The integration of advanced technologies like Apache Spark, and data mining algorithms enables efficient processing of these complex datasets, improving the accuracy of predictions and enhancing decision-making capabilities for disaster risk reduction.

# C.	Motivation for the Problem 
The motivation for developing this platform is rooted in the pressing need for enhanced climate resilience strategies in Canada. The project's focus is not just on developing a wildfire prediction tool but on providing a comprehensive solution that addresses multiple climate risks, making it unique in its approach. While similar platforms exist such Climate Atlas [4], Climate Action Tracker [5] etc., they often lack the integration of multiple hazards and the ability to adapt to Canada’s specific climate challenges. By developing a tool that uses predictive modeling, geospatial data analysis, and scalable cloud-based infrastructure, this project differentiates itself by offering a versatile and adaptive solution.
This project is particularly challenging and rewarding because it involves handling vast, unstructured datasets and integrating advanced technologies like Apache Spark for efficient data processing. The platform’s development will not only advance the technological landscape but also provide tangible benefits to government agencies, policymakers, and local communities by equipping them with the tools needed for informed decision-making. By supporting disaster risk reduction and promoting sustainable development, this project has the potential to make a significant impact on Canada’s climate resilience efforts, making it both timely and necessary.

# D.	Uniqueness of Our Work 
This platform distinguishes itself from existing solutions through its multi-hazard approach and advanced technological architecture. Unlike traditional systems that rely on static visualizations, our platform uses dynamic data analysis and predictive modeling to provide actionable insights for stakeholders, allowing for proactive decision-making. The integration of cloud computing solutions ensures the platform’s scalability, enabling future enhancements such as the addition of new climate variables and collaboration with international climate agencies.
Moreover, the platform is designed to be adaptive to Canada’s specific climate challenges. By incorporating historical data and advanced modeling, it addresses the need for precise and localized risk assessments, focusing not only on wildfire but also on other critical hazards like floods and heatwaves. This comprehensive approach supports Canada’s national climate action goals and contributes to global efforts in climate resilience and sustainable development, ensuring that communities and ecosystems can better withstand and recover from future climate-related events.

# II.	Literature Review

Natural hazards, such as wildfires and floods, present profound global challenges, necessitating the development of sophisticated models and comprehensive frameworks for accurate prediction and effective management. This literature review rigorously analyzes three key studies that focus on predictive wildfire modeling, multi-hazard risk assessment, and the impact of rainfall and soil moisture on flood trends. Each study is critically evaluated to uncover both its contributions and limitations, providing a foundation for the advancements proposed in our course project.
The study by Oulad Sayad et al. [6] presents an advanced machine learning-based model designed to predict wildfires using satellite data, incorporating Artificial Neural Networks (ANN) and Support Vector Machines (SVM). By harnessing big data from remote sensing technologies, the researchers utilized critical variables like the Normalized Difference Vegetation Index (NDVI) and Land Surface Temperature (LST), achieving remarkable accuracy rates of 98.32% for ANN and 97.48% for SVM. While the study effectively demonstrates the potential of combining remote sensing with machine learning, it reveals significant constraints due to its reliance on satellite data, which can be affected by cloud cover and sensor issues, leading to inconsistent data. Moreover, the geographic focus on Canadian forests restricts the model’s applicability elsewhere, requiring extensive recalibration for other ecosystems, thus impacting its scalability. Our project addresses these critical gaps by incorporating multiple data sources beyond satellite imagery, ensuring continuous and reliable local environmental monitoring. By leveraging diverse data inputs, our platform significantly reduces dependency on satellite data and enhances adaptability across different ecosystems, thereby offering a more robust and scalable solution for global applications.
Stalhandske et al. [7] provide a comprehensive framework for multi-hazard risk assessment, focusing particularly on river floods (RF) and tropical cyclones (TC). Their research utilizes the CLIMADA platform, an open-source tool that integrates physical drivers and recovery processes, offering a versatile risk assessment framework adaptable across various geographical contexts. This framework effectively illustrates how multi-hazard risk can be evaluated on both national and global scales, demonstrating its utility for policymakers. Despite these strengths, the study is limited by its static recovery assumptions, which presume full recovery by the end of each calendar year. This static approach does not account for the complex, real-world dynamics of recovery that may be prolonged or disrupted by consecutive disasters, especially in regions with socio-economic constraints. To overcome these limitations, our project introduces a dynamic recovery model that incorporates socio-economic variables such as population displacement rates and regional economic recovery timelines. This enhancement ensures that the model adapts more realistically to diverse regional conditions, making risk assessments more actionable and precise for stakeholders.
A comprehensive analysis of flood magnitudes in Australia highlights a trend where flood peaks have diminished despite increased rainfall intensity [8]. The researchers conducted an in-depth study of long-term data, encompassing streamflow, rainfall, and soil moisture levels, demonstrating that declining antecedent soil moisture significantly influences flood peaks. The findings emphasize the crucial role of soil moisture in flood prediction. However, the study’s dependence on historical data and the assumption of consistent soil moisture trends fail to account for potential future variability caused by land use changes, urban development, and evolving vegetation patterns. Furthermore, the model’s exclusion of projected climatic changes restricts its long-term applicability, reducing its reliability for future planning. In response, our project incorporates future projections for land use, vegetation changes, and climate scenarios, ensuring our models are not only adaptive but also aligned with evolving environmental conditions. By integrating predictive modeling that includes these variables, our approach provides a more robust and forward-looking solution for flood risk management, allowing policymakers to make informed decisions based on accurate, adaptable data.
The World Meteorological Organization (WMO) document [9] identifies several systemic limitations impacting the effectiveness of climate resilience models. It highlights the challenges in integrating and maintaining observation networks, particularly in the tropics, where data gaps can severely affect prediction accuracy. Moreover, many existing models rely on static recovery assumptions that fail to account for real-world dynamics, especially in areas experiencing consecutive disasters. High-resolution data, crucial for accurate modeling, remains limited due to computational and financial constraints. The report also emphasizes the need for interdisciplinary collaboration across meteorology, hydrology, and other fields, which is currently insufficient due to the absence of unified strategies. Addressing these limitations is essential for advancing predictive models and improving climate resilience. Our platform tackles these issues by leveraging cloud-based solutions and open-source technologies, enabling more accessible, scalable, and accurate climate risk predictions, even in data-sparse regions.
An additional document from the Asian Development Bank (ADB) discusses specific challenges associated with using digital technologies (DTs) in climate action [10]. While technologies such as satellite imagery and AI provide valuable data and predictive modeling capabilities, they face geographical constraints like cloud cover and accessibility issues in remote regions. Implementation in developing areas is further hindered by inadequate digital infrastructure and limited financial resources. Regulatory barriers and proprietary technologies also pose accessibility challenges, restricting the scalability of solutions. Our platform addresses these issues by prioritizing open-source technology and integrating publicly available data, ensuring our solution is scalable, adaptable, and accessible even in resource-constrained environments.
Overall, the reviewed studies and documents offer significant insights into predictive modeling and risk assessment for natural hazards, illustrating advancements in areas such as big data integration, multi-hazard frameworks, and soil moisture variability. However, the identified limitations underscore the need for models that adapt dynamically to evolving conditions, such as real-time data integration for wildfire prediction, dynamic recovery processes for multi-hazard assessments, and future variability considerations in flood prediction models. Our project builds upon these findings by integrating these dynamic variables, enhancing the scalability, precision, and generalizability of hazard predictions, ultimately contributing to a more comprehensive and resilient climate risk management platform.

# III.	Proposed Model / Implementation Details

The climate resilience data platform is a sophisticated, web-based solution that provides predictive modeling and risk assessment capabilities for multiple climate hazards, including wildfires and floods. The platform integrates a wide range of publicly available datasets via APIs, processes this data through advanced backend algorithms, and visualizes information through an intuitive and interactive web interface. This section elaborates on the platform’s architecture, workflow, and features, highlighting how it differentiates itself from existing solutions.
# A.	Overall Model Explanation
The platform's architecture is built on several critical components, each designed to work cohesively:
Data Collection Module: 
The platform integrates with external APIs, such as those provided by Environment and Climate Change Canada and the Government of Canada’s Open Data Portal, to collect comprehensive environmental data. This includes:
•	Weather Data: Temperature, humidity levels, and wind patterns.
•	Historical Wildfire Records: Information on past occurrences, intensity, and geographical impact.
•	Rainfall Patterns: Real-time updates on precipitation levels.
•	Soil Moisture Levels and Vegetation Indices: Data on soil conditions and vegetation health, critical for wildfire and flood prediction.
The data collection module refreshes this information every 24 hours, ensuring accuracy and timeliness, and stores it in MongoDB’s time-series collections for optimized retrieval.
Data Processing and Prediction Engine:
Using Python-based algorithms like Long Short-Term Memory (LSTM) models for time-series analysis and DBSCAN for clustering high-risk zones, the platform processes ingested data to perform predictive modeling. These models leverage:
•	Statistical Techniques: Identifying patterns and correlations between historical and real-time data.
•	Machine Learning Algorithms: Assessing variables such as temperature, precipitation, soil moisture, and vegetation cover to predict wildfire and flood risks accurately.
The platform extends these algorithms with a hybrid approach, integrating an Attention Mechanism with LSTM to enhance focus on critical variables and improve prediction precision.
Visualization Layer:
The processed data is visualized through an interactive web-based dashboard utilizing libraries like Leaflet.js for geospatial mapping. The platform displays risk levels in various regions, allowing users to:
•	Explore specific regions in Canada, drill down into risk assessments, and visualize changes over time.
•	Interact with the map to adjust parameters (e.g., selecting a specific timeframe or hazard type) for customized visualization.
D3.js is integrated to create dynamic, animated graphs and charts, providing engaging and informative user experience.
User Interface Module:
The platform’s user interface (UI) is developed for ease of use, offering users multiple filters and options to explore the data. Key features include:
•	Region-based Filters: Users can select specific regions or provinces in Canada to focus on localized climate risks.
•	Timeframe Adjustments: Users can adjust the timeframe (e.g., next 7 days, historical data over the last decade) to see how risks evolve.
•	Hazard Comparison: The UI allows for side-by-side comparison of different hazards (e.g., wildfire vs. flood risk) to provide a comprehensive overview.
Users can also access detailed reports, customize data visualizations, and receive instant notifications about critical climate risks directly within the dashboard.
# B.	Workflow Diagram
The platform follows a structured and efficient workflow for processing and visualizing data:
Data Ingestion:
The platform connects to trusted environmental agencies’ APIs to collect data on temperature, precipitation, vegetation cover, and historical climate events. This data is stored and managed within MongoDB’s time-series collections and geospatial indexes to optimize access and processing speed.
Data Processing:
Ingested data is pre-processed using MongoDB’s aggregation pipelines, where data cleaning and transformation occur to standardize inputs. The prediction engine applies machine learning models (e.g., LSTM with an attention mechanism) that analyze and correlate variables to forecast wildfire and flood risks.
The processing module incorporates anomaly detection algorithms (e.g., Isolation Forest) to identify unusual or extreme weather patterns.
Risk Assessment and Prediction:
The processed data is inputted into prediction models that generate risk levels for wildfires and floods. The platform applies advanced statistical methods and machine learning techniques to provide accurate and reliable forecasts for the upcoming week. Visual and numerical outputs are generated for user interpretation.
Data Visualization:
The output from prediction models is visualized on the platform’s dashboard. Users interact with the map to explore risk levels across regions, compare hazards, and generate reports based on selected criteria. The visualization is powered by Leaflet.js and D3.js, providing real-time updates and customization options.
The diagram below [Fig. 1.] illustrates the end-to-end data flow from ingestion (via APIs) to processing (prediction engine) and visualization (user interface). Each step is designed to ensure timely, accurate, and accessible climate risk predictions for the users.
 
# C.	Differentiation from Existing Works
Existing climate risk platforms often focus on single hazards, such as wildfire prediction or flood monitoring, and typically use static data models that lack adaptability. In contrast, our platform offers:
•	Multi-Hazard Integration: Combines wildfire and flood risk assessments in a single interface, allowing users to view and compare multiple risks at once.
•	Dynamic Data Models: The platform uses dynamic, real-time updates from APIs and incorporates multiple environmental variables (e.g., soil moisture, vegetation, rainfall) into its models, providing a holistic view.
•	Geospatial and Time-Series Analysis: Unlike models heavily reliant on satellite data, which can be inconsistent, our platform leverages a diverse range of data sources from open databases and APIs, ensuring continuous updates and reducing data gaps.
•	Unique Hybrid Modeling: The use of LSTM with Attention Mechanisms and a hybrid anomaly detection system (Isolation Forest + LOF) provides advanced adaptability and sensitivity not commonly found in traditional models.

# D.	Feature Explanation
The platform includes the following detailed features:
•	Wildfire Risk Prediction Module: Uses historical weather data and vegetation indices to predict wildfire risks. Incorporates real-time data through APIs, updating risk levels and visualizing them on a dynamic map interface.
•	Flood Risk Assessment Tool: Analyzes rainfall data, soil moisture levels, and historical flood records. Updates weekly to reflect changes in rainfall intensity and patterns and visualizes flood risk levels through geospatial mapping.
•	Multi-Hazard Dashboard: Integrates data for multiple hazards (wildfires and floods) into a unified interface, offering a comparative view with customizable filters for time, region, and hazard type.
•	Customizable Reports: Allows users to generate reports summarizing risk levels over chosen periods and regions. Reports include interactive maps and statistical graphs, downloadable in PDF format.
•	User Alerts and Notifications: Provides notifications within minutes of detecting high-risk events, ensuring users receive timely, critical information directly on the dashboard or via email alerts.
IV.	System Definition (Functional Requirements)
The climate resilience data platform is designed as a web-based solution that offers predictive modeling and risk assessment capabilities for various climate hazards. The functional requirements for this system are as follows:
A.	Wildfire Risk Prediction Module:
Objective: To predict wildfire occurrences with at least 85% accuracy using historical data and publicly available weather datasets.
Function: This module analyzes historical climate data, such as temperature, precipitation, and vegetation indices, sourced from open APIs (e.g., Environment and Climate Change Canada). It provides risk assessments and visualizes predicted risk levels on an interactive map, with updates based on the latest available data.
Output: A dynamic map interface highlighting high, medium, and low wildfire risk zones, accessible via the platform’s dashboard.
B.	Flood Risk Assessment Tool:
Objective: To assess flood risks with an accuracy rate of 80% by analyzing rainfall data and historical flood records.
Function: The tool leverages publicly available datasets from government and environmental agencies to calculate flood risk levels based on rainfall trends and historical flood events. It provides regular updates on risk levels to inform users about potential flood threats.
Output: Visual flood risk indicators on the platform’s map interface, with options to view both historical flood data and current risk levels.
C.	Multi-Hazard Dashboard:
Objective: To integrate data from at least two climate hazards (wildfires and floods) and provide users with a comparative analysis feature.
Function: The dashboard combines data from multiple sources, presenting visualizations for each hazard type in a single interface. It allows users to compare risk levels for different hazards within selected regions and time frames using interactive tools.
Output: An interactive web-based dashboard displaying hazard comparisons, with filters for customizing views by location, hazard type, and period.
D.	Geospatial Data Visualization:
Objective: To visualize geospatial data with a response time of under 2 seconds for datasets up to 10 GB.
Function: The platform uses web-based geospatial libraries (e.g., Leaflet.js or Mapbox) to visualize climate risk data on an interactive map. Users can zoom, pan, and explore specific regions to view detailed hazard information.
Output: An interactive map with multiple data layers for users to visualize vegetation cover, rainfall intensity, and hazard risk levels in selected regions.
E.	Data Source Integration via APIs:
Objective: To integrate with at least three external APIs (e.g., Environment and Climate Change Canada, Government of Canada’s Open Data Portal) to update climate data every 24 hours.
Function: The platform uses APIs to pull real-time updates from these data sources, ensuring that the information displayed is current and accurate. Data caching mechanisms are implemented to optimize performance and minimize API calls.
Output: Automated daily updates to the platform’s database, with logs tracking data refresh rates and API connections.
F.	Customizable User Interface:
Objective: To provide an interface that allows users to customize their view based on region, hazard type, and time frame with a response time of under 1 second per interaction.
Function: The platform offers a customizable interface, including dropdowns for selecting regions and hazard types. Users can access historical data, current risk levels, and filter the results according to their preferences.
Output: A responsive web interface offering personalized data views and real-time interaction, ensuring an intuitive and user-friendly experience.
G.	User Alerts and Notifications:
Objective: To implement an alert system that notifies users of high-risk situations through in-platform notifications.
Function: The platform displays alerts directly within the user interface when it detects high-risk situations (e.g., wildfire threats or flood warnings). Notifications are integrated within the dashboard, providing quick access to relevant data visualizations.
Output: Real-time notifications displayed within minutes of hazard updates, ensuring that users receive critical information promptly.
H.	Report Generation and Data Export:
Objective: To generate customized reports summarizing risk levels for selected regions and time periods within 5 seconds, with support for exporting in PDF format.
Function: The platform includes a report generation feature, allowing users to compile visual and statistical data into comprehensive reports. Users can select parameters such as region, time frame, and hazard type before exporting.
Output: Downloadable PDF reports featuring maps, graphs, and summaries, accessible directly from the platform’s dashboard.
I.	Data Analysis and Historical Trends:
Objective: To provide a tool that allows users to analyze historical trends in climate data over a 10-year period for wildfires and floods.
Function: The platform supports historical data analysis, enabling users to explore trends such as temperature variations, rainfall patterns, and vegetation changes. It also allows for comparison of historical data with current conditions.
Output: Interactive graphs and charts displaying historical and current climate data, supporting informed comparisons and predictive analyses.

# References
[1] 	Natural Resources Canada, "Canada in a Changing Climate: Synthesis Report," Natural Resources Canada, 2023.
[2] 	Natural Resources Canada, "Canada's Record-Breaking Wildfires: 2023, a Fiery Wake-up Call," 2023. [Online]. Available: https://natural-resources.canada.ca/simply-science/canadas-record-breaking-wildfires-2023-fiery-wake-call/25303. [Accessed September 2024].
[3] 	Canadian Climate Institute, "Climate Change and Wildfires in Canada," Canadian Climate Institute, 2024.
[4] 	"Climate Atlas of Canada," Prairie Climate Centre, [Online]. Available: https://climateatlas.ca/. [Accessed October 2024].
[5] 	"Climate Action Tracker," Climate Action Tracker, [Online]. Available: https://climateactiontracker.org/countries/. [Accessed October 2024].
[6] 	H. M. H. A. M. Younes Oulad Sayada*, "Predictive Modeling of Wildfires: A New Dataset and Machine," Remote Sensing Letters, vol. 10, no. 7, pp. 645-655, 2019. 
[7] 	C. B. S. S. M. I. J. S. T. V. D. N. B. a. C. M. K. Z. Stalhandske, "Global multi hazard risk assessment in a changing climate," Scientific Reports, vol. 14, no. 5875, pp. 1-13, 2024. 
[8] 	R. N. Conrad Wasko, "Influence of changes in rainfall and soil moisture on trends in flooding," Journal of Hydrology, vol. 575, pp. 432-441, August 2019. 
[9] 	W. M. O. (WMO), "Challenges and Opportunities in Research on Climate, Weather, Water and Environment," World Meteorological Organization (WMO), Geneva, 2009.
[10] 	A. D. B. (ADB), "Digital Technologies for Climate Action, Disaster Resilience, and Environmental Sustainability," Asian Development Bank, Mandaluyong City, Metro Manila, Philippines, 2021.



![image](https://github.com/user-attachments/assets/a9e00b74-bf45-42a4-b6b1-55aeef49ec1b)

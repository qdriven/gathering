Glossary "A"
activity
An ecoinvent activity dataset represents a unit process of a human activity and its exchanges with the environment and
with other human activities. There are several activity types in the ecoinvent v3 database;transforming activities,
treatment activities, market activity, import and export activities, production and supply mixes, etc.

activity class
Group of activities classified together under a heading in a statistical classification of activities, such as ISIC (
International Standard Industrial Classification).

activity link (=direct link)
A link for a specific exchange to a specific supplying dataset for that exchange as provided by the dataset author, as
opposed to the links automatically added by the database service layer during linking of the system models.

In general, data providers do not need to supply activity links, since these are automatically added by the database
service layer. However, if a specific group of enterprises are so closely linked in a supply chain that the production
volumes of the specific suppliers can be shown to fluctuate with the demand of the specific customers, data providers
shall add activity links to reflect this specific link.

The reason for linking directly to a specific supplying activity is provided in the comment field for the linked
exchange. When transforming activities are linked directly, thus avoiding the market activities, the activities and data
that are normally included with the market activities, are instead added directly to the activity requiring the input.

addition to stock
By-product or waste with a lifetime in excess of one year. See also under infrastructure.

AOX
Abbreviation for Adsorbable Organic Halogen Compounds

Glossary "B"
biological oxygen demand (BOD)
Amount of dissolved oxygen needed by aerobic decomposers to break down the organic materials in a given volume of water
at a certain temperature over a specified time period.

BOD
Abbreviation for biological oxygen demand

by-product / waste
Any activity output that is neither a reference product nor an exchange to the environment.

Glossary "C"
CED
Abbreviation for Cumulative Energy Demand

chemical oxygen demand (COD)
An indirect measure of the amount of oxygen used by inorganic and organic matter in water. The measure is a laboratory
test based on a chemical oxidant and therefore does not necessarily correlate with biochemical oxygen demand.

child dataset
In child datasets values can be set to relate to the corresponding value in the parent dataset. When such a related
value is changed in the parent dataset it is automatically changed in the child dataset as well. Only geographical
inheritance is allowed in the ecoinvent v3 database, i.e. some regional datasets (such as Brazilian soybean production)
might be modelled as a child dataset of the global dataset.

CIF
Abbreviation for Cost Insurance and Freight

conditional exchange
Exchange that is only activated for a specified system model.

constrained market
A market where all or part of a change in demand is not reflected in a corresponding change in supply, but instead in a
change in consumption elsewhere.

Constrained market datasets include a conditional exchange with a direct activity link to the consumption activity that
is affected by the change in demand. This exchange is activated only for specific system models that take into account
market constraints, e.g. the consequential system model.

When the system model “allocation, ecoinvent default” is chosen, the conditional exchange is not activated and the
constrained markets behave like any other markets.

To understand how this market behaves during consequential linking, please see the Data Quality Guideline.

consumed water (=water consumption)
Water withdrawal where release back to the source does not occur, e.g. due to evaporation, evapotranspiration, product
integration or discharge into a different drainage basin or the sea.

consumption mix
The output from a market activity.

cooling water
Water that is used to regulate the temperature of a process. This type of water in most cases does not come in contact
with the product.

CPC (Central Product Classification);
Constitutes a comprehensive classification of all products, including goods and services. The central product
classification is a classification based on the physical characteristics of goods or on the nature of the services
rendered; each type of good or service distinguished in the CPC is defined in such a way that it is normally produced by
only one activity as defined in ISIC. The CPC classification is used by the ecoinvent Centre for classification of
products (intermediate exchanges) present in the ecoinvent database.

CV
Abbreviation for Coefficient of Variance

Glossary "D"
data quality guidelines
The data quality guidelines are the cornerstone document of ecoinvent version 3 database providing a complete
documentation and explanation of the principles and rules for ecoinvent version 3.

database service layer
The ecoinvent database consists of unlinked single or multi-output datasets on unit process level. These datasets are
linked based on the system model chosen. Linking is performed by the so-called database service layer. The database
service layer is a group of mathematical formulas, commands and validation rules specific to a chosen system model.

DM
Abbreviation for dry mass

DOC
Abbreviation for dissolved organic carbon

dry mass
Dry mass represents the dry material of a sample or of an object when completely dried; dry mass is not the same as ash
content – it does include chemically bound H and O.

Glossary "E"
ecoEditor
A software available for free on the ecoinvent website. This tool is recommended to be used to create LCI datasets in
ecoSpold2 format and submitting LCI data to the ecoinvent database.

ecoinvent database version 2
An older version of the ecoinvent database.

ecoinvent database version 3
The current version of the ecoinvent database.

ecoQuery
A web user interface through which all the users of the ecoinvent database can access the database (registration
required). Even users usually accessing the ecoinvent database through LCA software tools (such as openLCA, SimaPro or
GaBi) can also always access the ecoinvent database through the ecoQuery. Users who did not purchase the ecoinvent
licence can still register as guests and see the meta data (description) of all the datasets available in the database.

Login at https://ecoquery.ecoinvent.org/

ecoSpold Format
ecoSpold is a name for a format used by ecoinvent to create life cycle inventories. This format sets up standards on
what are mandatory and what are optional fields for a standard life cycle inventory. While the ecoSpold 1 format is used
for ecoinvent version 1 and 2, it is the ecoSpold2 format for ecoinvent version 3. The ecoSpold2 format offers many new
fields, such as mathematical relation, variable names or properties of an exchange which were not available in the older
ecoSpold1 format.

ecoSpold2 format

elementary exchange
Exchange with the natural, social or economic environment. Examples: Unprocessed inputs from nature, emissions to air,
water and soil, physical impacts, working hours under specified conditions.

evaporation
The process in which water changes from a liquid to a gas state.

evaporation rate
The ratio of the amount of water evaporated during the process to the amount of water entering the process.

evapotranspiration
The evaporation of water from a vegetated surface through the combined processes of soil evaporation and plant
transpiration.

exchange
Two basic types of exchanges exist – elementary exchanges and intermediate exchanges.

Glossary "F"
FOB
Abbreviation for Free On Board

Fresh water
Water having low concentration of salts.

FromEnvironment
Represents the type (origin) of an exchange. This is an elementary exchange (with the environment) present as an input
of an activity.

FromTechnosphere
Represents the type (origin) of an exchange. This is an intermediate exchange (with the technosphere) present on the
input of an activity.

Glossary "G"
GDP
Abbreviation for Gross Domestic Product

Geography
The term “geography” refers to a geographic region in the context of ecoinvent. This can be the whole world (global,
GLO), a region of several countries (e.g. Europe, RER), one country (e.g. Germany, DE) or a smaller area (e.g. a
province in Canada). Activities are always valid for certain geography.

List of geographies present in ecoinvent version 3 can be accessed here
including name, shortcut, id and coordinates

GLO
Abbreviation for global

groundwater
Water contained in aquifers which are strata in which the water is contained in the porous voids (saturated zone).

groundwater depletion
Rate of groundwater abstraction in excess of natural recharge rate.

Glossary "I"
ID
Abbreviation for Identifier

inheritance
Passing on of field contents from a parent dataset to a child dataset. Only geographical inheritance is allowed in the
ecoinvent version 3 database, i.e. some regional datasets (such as Brazilian soybean production) might be modelled as a
child dataset of the global dataset. When a value is changed in the parent dataset it is automatically changed in the
child dataset as well.

intermediate exchange
An exchange between two activities that stays within the technosphere and is not emitted to or taken from the
environment.

International Standard Industrial Classification
The United Nations system for classifying economic data. ISIC is a basic tool for studying economic phenomena, fostering
international comparability of data, providing guidance for the development of national classifications and for
promoting the development of sound national statistical systems (UN). ISIC provides a classification system for
activities and products that ecoinvent has adopted for version 3.

IO
Abbreviation for Input Output, economic model

ISIC
Abbreviation for International Standard Industrial Classification

ISO
Abbreviation for International Organization of Standardization

Glossary "K"
KML
Abbreviation for Keyhole Markup Language

Glossary "L"
LCA
Abbreviation for Life Cycle Assessment

LCI
Abbreviation of Life Cycle Inventory

LCIA
Abbreviation for Life Cycle Impact Assessment

LCIA score
Abbreviation for Life Cycle Impact Assessment score. One LCIA score is one LCIA indicator for one dataset, for example
IPCC2013 Global Warming Potential (GWP) 100a for “mango production, BR”. If you consider IPCC2013 GWP100a and EF3.0 land
use (soil quality index) for “mango production, BR”, this counts as two indicators for one dataset, i.e., two LCIA
scores.

Life Cycle Assessment (LCA)
The compilation and evaluation of the inputs, outputs and the potential environmental impacts of a product system
throughout its life cycle (ISO 1440:2006).

Life Cycle Impact Assessment (LCIA)
The phase of life cycle assessment aimed at understanding and evaluating the magnitude and significance of the potential
environmental impacts for a product system throughout the life cycle of the product (ISO 14040:2006).

Life Cycle Inventory (LCI)
The phase of life cycle assessment involving the compilation and quantification of inputs and outputs for a product
throughout its life cycle (ISO 14040:2006).

lifetime of a product
The period between the time of production and the time of initiating waste treatment of the product.

linking
The ecoinvent version 3 database contains unlinked datasets on unit process level (UPR). These unlinked datasets can be
linked through the markets using different system models.

For more details see our FAQs
Data Quality Guidelines

Glossary "M"
market activity
A market activity transfers a product or service (intermediate exchange) from one or more transforming activities that
produce it, to the transforming activities that consume it.
Whether a transforming activity supplies a given market activity is determined by their geographies. A market activity
may cover either the global geography (GLO) or a specific region. The general rule is that a market is supplied by
transforming activities that are located within the same geographical boundaries, and whose product is not consumed
entirely by another transforming activity (through a direct activity link). The shares supplied by each transforming
activity are determined by their production volumes. However, markets for which more detailed information is available
may have their shares specified manually for each system model.

A market activity therefore provides the average consumption mix of a product for a given region, and the marginal
consumption mix in the case of system models that use marginal suppliers.

In addition to the product or service that is transferred, a market activity may contain exchanges that model the
average transportation of the product, direct emissions caused by the transportation, as well as an input from the
market itself, which represents losses that occur during transportation and storage of the product.

More information about market activities is provided on this page.

mft / non-mft
mft stands for “material for treatment”, non-mft satnds for “material not for treatment”. These are the two categories
by which products are classified in the APOS system model. As the name implies, a “material for treatment” requires to
be treated in a treatment activity in the linking of the APOS system model, while this is not the case for non-mft
classified products. For example the mft “municipal solid waste” calls “treatment of municipal solid waste,
incineration” and other treatment activities through the “market for municipal solid waste”.)

Read more about the APOS system model and its linking rules here.

MO
Abbreviation for multi-output activity

multi-output activity
An activity with more than one output.

Glossary "N"
NAICS
Abbreviation for North American Industry Classification System

NDI
Abbreviation for National Data Collection Initiative

NMVOC
Abbreviation for Non-Methane Volatile Organic Compound

NPP
Abbreviation for Net Primary Productivity

NPP-C
Abbreviation for Net Primary Productivity Carbon

Glossary "P"
parameter
represents different types of values used in a dataset and defined by the data provider. The new ecoSpold2 data format
allows the use of formulas to calculate the amounts of flows and other entities in the datasets. For example the yield
of chemical reaction can be inserted in the dataset as a parameter.

parent dataset
A dataset referred to by a child dataset as the dataset from which field values in the child dataset are to be inherited
to the extent defined, i.e. parent datasets serve as basis of their associated child datasets. Only geographical
inheritance is allowed in the ecoinvent version 3 database, i.e. some regional datasets (such as Brazilian soybean
production) might be modelled as a child dataset of the global dataset. In child datasets values can be set to relate to
the corresponding value in the parent dataset. When such a related value is changed in the parent dataset it is
automatically changed in the child dataset as well.

PM10
Abbreviation for particulate matter with a diameter of less than 10 µm

PM2.5
Abbreviation for particulate matter with a diameter of less than 2.5 µm

process
A term used in ecoinvent version 2 which was replaced in ecoinvent version 3 by the more generic term activity. Process
represents set of interrelated or interacting activities that transforms inputs into outputs (ISO 14040).

process water
Water used by a process excluding cooling water. In most cases, process water is in contact with the product. This water
does not include incorporated water in inputs used by the process.

produced water
This can occur in the case of some chemical reactions.

product
Good or service output of a human activity with a positive either market or non-market value. While in ecoinvent version
2 the product name was identical with the activity name, in ecoinvent version 3 the product name is independent from the
activity name. For example in ecoinvent version 2 “chloroacetic acid, at plant” is a name for both the activity and the
product. The same dataset in ecoinvent version 3 is called “chloroacetic acid production” which produces the product
called “chloroacetic acid”.

product water content
This is the flow from another process in the system (technosphere flow). Every product has water content and therefore
can be used to balance the water flows. This is especially important for water transport and treatment processes (e.g.
water supply and waste water treatment). The product water content is presented in the ecoinvent version 3 database via
the water in wet mass property.

production mix
The production-volume-weighted average of the suppliers of a specific product within a geographical area.

property
Every exchange (both elementary and intermediate) with a mass can have a number of properties. For example, every
product currently present in the database has at least the following properties; wet mass, dry mass, water in wet mass,
water content, carbon content, fossil and carbon content, non-fossil.

Glossary "R"
rest of the world (RoW)
A dynamic concept that exists in the situation when both a global dataset and one or more non-global datasets are
available for the same activity, time period, and macro-economic scenario. The definition is specific to each activity
and depends on what defined geographies are available for the specific activity name. The activities with the
Rest-of-the-World geographic location are generated automatically during the linking by the database service layer. In
ecoinvent v3.2 (2015) and higher the RoW is generated as an exact copy of the GLO dataset with uncertainty adjusted. The
newly generated RoW is then linked with activities of an adequate geographies creating RoW specific supply chain.

RoW
Abbreviation for rest of the world

Glossary "S"
salt water
Water having high concentration of salts.

service
A product without a mass.

shallow groundwater
Groundwater that is located less than three meters deep.

SPOLD
Abbreviation for Society for the Promotion of Lifecycle Development

supply mix
A production mix with the addition of the import of the specified product to the geographical area.

surface water
Fresh water you can see as overland flow, rivers and lakes excluding sea water. A distinction is not made between lake
and river water.

system model
A model describing how activity datasets are linked to form product systems. A system model may determine factors such
as whether to use allocation (and which type of allocation) or substitution to handle the multi-functionality problem,
or whether to use average or marginal suppliers. It may also affect how by-product treatments are assessed. Synonym (
input-output economics): Technology model.

Glossary "T"
TCDD
Abbreviation for tetra-chlor-dibenzo-dioxin

TDS
Abbreviation for Total Dissolved Solids

technosphere
Represents all human activities. An exchange of a certain activity can be between the activity and the environment (
elementary exchange, for example CO2 emission to air) or between two activities (intermediate exchange, for example
wastewater to be released from one activity to another – treatment of wastewater).

TOC
Abbreviation for Total Organic Carbon

ToEnvironment
Represents the type (origin) of an exchange. This is an elementary exchange (with the environment) present as an output
of an activity.

ToTechnosphere
Represents the type (origin) of an exchange. This is an intermediate exchange (with the technosphere) present on the
output of an activity.

TPM
Abbreviation for Total Particulate Matter

transforming activity
A human activity that transforms inputs into outputs that are different from the inputs. This is the most common type of
activity in the ecoinvent database, e.g. a hard coal mine that transforms hard coal in ground to the marketable product
hard coal, or an automobile plant that turns metals, plastics and energy into cars.

treatment activity
A transforming activity with a reference product with a negative sign, which effectively means that the activity is
supplying the service of treating or disposing of the reference product. E.g. the reference product of treatment of
waste plastic activity is -1kg of waste plastic. The name of a treatment activity always start with “treatment of …”
phrase.

TSS
Abbreviation for Total Suspended Solids

Glossary "U"
UN
Abbreviation for United Nations

unit process (UPR)
The smallest element considered in the life cycle inventory analysis for which input and output data are quantified (ISO
14040), often also referred to as “gate-to-gate” process.

The database contains data on a unit process level that are neither vertically nor horizontally aggregated. However, we
seek to avoid the separate reporting of unit processes when this does not add any useful information in an LCA context.
This is the case when one unit processes always supplies all of its products directly to another specific unit process
at the same location, so that the product of the first unit process never appears as a marketable product, and cannot be
supplied by an external supplier.

UUID
Abbreviation for Universally Unique Identifier

Glossary "W"
water balance
Water input – water output = 0. Actual water balance is the difference between the amount of water on the input and the
amount of water on the output. Ideal water balance occurs when the amount of water on the input if equal to the amount
of water on the output.

water content (U)
The ratio between water in wet mass and dry mass. Water content = water in wet mass /dry mass.

water footprint
Life cycle impact indicator that assesses the contribution of products and services to water related impacts on the
environment.

water in wet mass (WWM)
The amount of water in the wet mass after subtracting the dry mass. Water in wet mass = wet mass – dry mass.

water inventory
Phase of a water footprint study involving compilation and quantification of inputs and outputs related to water use for
products, processes and organisations.

water supply flows
= water supply exchanges; are water exchanges with the technosphere (such as tap water).

water use
Generic term used to describe human activity involving water resources (including agriculture, industry, energy
production, public sector and households, in stream and in-situ uses such as fishing, recreation, transportation and
waste disposal) as well as the total amount of water used during the process.

water use, direct
Refers to process flows directly related to a given process.

water use, indirect
Refers to process flows indirectly related to a given process, for example water use related to electricity production
used during the process.

water withdrawal
Anthropogenic removal of water from any water body, either permanently or temporarily.

wet mass (WM)
The wet matter of a sample or of an object. Wet mass = dry mass +water in wet mass.

Glossary "X"
XML
Abbreviation for Extended Markup Language


A
-

[activity](/glossary-terms/#!/activity)

[activity class](/glossary-terms/#!/activity_class)

[activity link (=direct link)](/glossary-terms/#!/activity_link)

[addition to stock](/glossary-terms/#!/addition_to_stock)

[AOX](/glossary-terms/#!/aox)

B
-

[biological oxygen demand (BOD)](/glossary-terms/#!/biological_oxygen_demand)

[BOD](/glossary-terms/#!/bod)

[by-product / waste](/glossary-terms/#!/by_product_waste)

C
-

[CED](/glossary-terms/#!/ced)

[chemical oxygen demand (COD)](/glossary-terms/#!/cod)

[child dataset](/glossary-terms/#!/child-dataset)

[CIF](/glossary-terms/#!/cif)

[conditional exchange](/glossary-terms/#!/conditional-exchange)

[constrained market](/glossary-terms/#!/constrained-market)

[consumed water (=water consumption)](/glossary-terms/#!/consumed-water)

[consumption mix](/glossary-terms/#!/consumption-mix)

[cooling water](/glossary-terms/#!/cooling-water)

[CPC (Central Product Classification);](/glossary-terms/#!/cpc)

[CV](/glossary-terms/#!/cv)

D
-

[data quality guidelines](/glossary-terms/#!/data-quality-guidelines)

[database service layer](/glossary-terms/#!/database-service-layer)

[DM](/glossary-terms/#!/dm)

[DOC](/glossary-terms/#!/doc)

[dry mass](/glossary-terms/#!/dry-mass)

E
-

[ecoEditor](/glossary-terms/#!/ecoeditor)

[ecoinvent database version 2](/glossary-terms/#!/ecoinvent-database-v2)

[ecoinvent database version 3](/glossary-terms/#!/ecoinvent-database-v3)

[ecoQuery](/glossary-terms/#!/ecoquery)

[ecoSpold Format](/glossary-terms/#!/ecospold-format)

[elementary exchange](/glossary-terms/#!/elementary-exchange)

[evaporation](/glossary-terms/#!/evaporation)

[evaporation rate](/glossary-terms/#!/evaporation-rate)

[evapotranspiration](/glossary-terms/#!/evapotranspiration)

[exchange](/glossary-terms/#!/exchange)

F
-

[FOB](/glossary-terms/#!/fob)

[fresh water](/glossary-terms/#!/fresh-water)

[FromEnvironment](/glossary-terms/#!/fromenvironment)

[FromTechnosphere](/glossary-terms/#!/fromtechnosphere)

G
-

[GDP](/glossary-terms/#!/gdp)

[Geography](/glossary-terms/#!/geography)

[GLO](/glossary-terms/#!/glo)

[groundwater](/glossary-terms/#!/groundwater)

[groundwater depletion](/glossary-terms/#!/groundwater-depletion)

I
-

[ID](/glossary-terms/#!/id)

[inheritance](/glossary-terms/#!/inheritance)

[intermediate exchange](/glossary-terms/#!/intermediate-exchange)

[International Standard Industrial Classification](/glossary-terms/#!/international-standard-Industrial-classification)

[IO](/glossary-terms/#!/io)

[ISIC](/glossary-terms/#!/isic)

[ISO](/glossary-terms/#!/iso)

K
-

[KML](/glossary-terms/#!/kml)

L
-

[LCA](/glossary-terms/#!/lca)

[LCI](/glossary-terms/#!/lci)

[LCIA](/glossary-terms/#!/lcia)

LCIA score

[Life Cycle Assessment (LCA)](/glossary-terms/#!/life-cycle-assessment)

[Life Cycle Impact Assessment (LCIA)](/glossary-terms/#!/life-cycle-impact-assessment)

[Life Cycle Inventory (LCI)](/glossary-terms/#!/life-cycle-inventory)

[lifetime of a product](/glossary-terms/#!/lifetime-of-a-product)

[linking](/glossary-terms/#!/linking)

M
-

[market activity](/glossary-terms/#!/market-activity)

[mft / non-mft](/glossary-terms/#!/mft-non-mft)

[MO](/glossary-terms/#!/mo)

[multi-output activity](/glossary-terms/#!/multi-output-activity)

N
-

[NAICS](/glossary-terms/#!/naics)

[NDI](/glossary-terms/#!/ndi)

[NMVOC](/glossary-terms/#!/nmvoc)

[NPP](/glossary-terms/#!/npp)

[NPP-C](/glossary-terms/#!/npp-c)

P
-

[parameter](/glossary-terms/#!/parameter)

[parent dataset](/glossary-terms/#!/parent-dataset)

[PM10](/glossary-terms/#!/PM10)

[PM2.5](/glossary-terms/#!/PM2-5)

[process](/glossary-terms/#!/process)

[process water](/glossary-terms/#!/process-water)

[produced water](/glossary-terms/#!/produced-water)

[product](/glossary-terms/#!/product)

[product water content](/glossary-terms/#!/product-water-content)

[production mix](/glossary-terms/#!/production-mix)

[property](/glossary-terms/#!/property)

R
-

[rest of the world (RoW)](/glossary-terms/#!/rest-of-the-world)

[RoW](/glossary-terms/#!/row)

S
-

[salt water](/glossary-terms/#!/salt-water)

[service](/glossary-terms/#!/service)

[shallow groundwater](/glossary-terms/#!/shallow-groundwater)

[SPOLD](/glossary-terms/#!/spold)

[supply mix](/glossary-terms/#!/supply-mix)

[surface water](/glossary-terms/#!/surface-water)

[system model](/glossary-terms/#!/system-model)

T
-

[TCDD](/glossary-terms/#!/tcdd)

[TDS](/glossary-terms/#!/tds)

[technosphere](/glossary-terms/#!/technosphere)

[TOC](/glossary-terms/#!/toc)

[ToEnvironment](/glossary-terms/#!/toenvironment)

[ToTechnosphere](/glossary-terms/#!/totechnosphere)

[TPM](/glossary-terms/#!/tpm)

[transforming activity](/glossary-terms/#!/transforming-activity)

[treatment activity](/glossary-terms/#!/treatment-activity)

[TSS](/glossary-terms/#!/tss)

U
-

[UN](/glossary-terms/#!/un)

[unit process (UPR)](/glossary-terms/#!/upr)

[UUID](/glossary-terms/#!/uuid)

W
-

[water balance](/glossary-terms/#!/water-balance)

[water content (U)](/glossary-terms/#!/water-content)

[water footprint](/glossary-terms/#!/water-footprint)

[water in wet mass (WWM)](/glossary-terms/#!/water-in-wet-mass)

[water supply flows](/glossary-terms/#!/water-supply-flows)

[water use](/glossary-terms/#!/water-use)

[water use, direct](/glossary-terms/#!/water-use-direct)

[water use, indirect](/glossary-terms/#!/water-use-indirect)

[water withdrawal](/glossary-terms/#!/water-withdrawal)

[water withdrawal](/glossary-terms/#!/water-withdrawal)

[wet mass (WM)](/glossary-terms/#!/wet-mass)

X
-

[XML](/glossary-terms/#!/xml)

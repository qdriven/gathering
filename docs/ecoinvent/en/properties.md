# Properties

The latest version of the ecoinvent database contains around 4,000 different products, including raw materials, goods
and services.

The same product can be produced from multiple technologies and in multiple locations, sometimes resulting in different
product properties, e.g., physical and chemical properties. For example, wood from different species may have different
densities, crude oil from different regions may have different heating values and different fractions of municipal waste
may have different carbon contents. Thus, every product with mass in the ecoinvent database comes with property
information.

## Product Properties in the ecoinvent database

Price is added as a property to every product of the database, except waste. The price represents a global and
long-term (typically five years) average, in Euros.
However, rapidly fluctuating market prices and externalities are not reflected in the price.
In the case of multi-output processes, the prices of the various outputs are used to determine the economic allocation
factor in the attributional system models. Exceptions may apply where physical product properties must be maintained:
heat and power co-generation processes are an example. These products are allocated taking into account the exergy of
the generated heat and electricity. The property of the economic allocation factor is called true value. Read more about
allocation in the system models section.

Additionally, six mandatory product properties are available for each product with mass:

- ***Dry mass***
  Dry mass is specified in the database for every product with mass. For substances other than water, dry mass is not
  the same as ash content but is calculated as the wet mass minus the water mass and thus includes chemically bound H
  and O. Inputs or outputs of water may therefore, somewhat counterintuitively, have a dry mass when the water is
  incorporated into or released from chemical reactions involving chemically bound H and O.
- ***Wet mass***
  The wet matter of a sample or of an object, wet mass = dry mass +water in wet mass, that is, the value used to
  calculate transport in the markets.
- ***Water content***
  The ratio between water in wet mass and dry mass.
  Water content = water in wet mass /dry mass
- ***Water in wet mass***
  The amount of water in the wet mass after subtracting the dry mass.
  Water in wet mass = wet mass – dry mass.
- ***Biogenic and fossil carbon content***
  The fossil and the non-fossil carbon contents are specified for every product with mass in the database; they are
  always given per dry mass (i.e., they are dimensionless properties).

Numerous optional product properties are specified where they are useful. Common examples include:

- ***The metal content of metal ores***
  Metal content, e.g., iron content of iron ore, is given per dry mass (i.e., it is a dimensionless property).
- ***The lifetime & lifetime capacity***
  The lifetime is the period between the time of construction and the time of initiating decommissioning of an
  infrastructure item. Lifetime capacity is the quantity of products or service units an infrastructure is capable of
  producing or performing over its entire lifetime at full utilisation. For example, this could be the kilometres driven
  by a car or the kilowatt hours produced by a power plant at full load.
  Example: The activity “lignite power plant construction, 500 MW” has a reference product of 1 unit of “lignite power
  plant”. The lifetime is defined as 34 years, and the capacity is defined as 300,000 hours of electricity production at
  full load. Hence, the lifetime capacity is 1.5E11 kWh (corresponding to 300,000 hours * 500 MW).This property is very
  useful for calculating the inputs of infrastructure to consumption activities: the electricity production activity
  will require 1 kWh/(0.68 * lifetime_capacity) = 9.8E-12 units of this input to produce 1 kWh of electricity.
- ***Heating value or energy content***
  Information on the energy content is provided by 2 properties, i.e. lower heating value (heating value, net) and
  higher heating value (heating value, gross). Lower heating values (LHVs) are specified for all relevant products, such
  as fuels, chemicals, and wood. LHVs are expressed as MJ per unit of reference product. The LHVs are quoted for
  materials at the specified water content. Higher heating values are provided for specific products such as fuels in MJ
  per kg of product. Heating values can either vary depending on the geographical or technological origin of the fuel or
  be standardised throughout the entire database. For example, the lower heating value of petroleum is defined as 43.2
  MJ/kg throughout the entire database.

## Why are properties useful

Product properties can serve many purposes, both within the database and for tailored tools and analysis.

Most prominently, properties for carbon content and the ability to distinguish between biogenic and fossil carbon are
essential to analyse carbon balances and carbon footprints.

Similarly, the mass and water properties in ecoinvent allow for thorough water balances and water footprinting.

The price property, which is available for all materials, goods and services, also allows for simple cost analysis, even
life cycle cost analysis (without externalities and human resource consumption).

When a product is produced with different properties in different locations or from different technologies, the
specification of the properties allows the supply from all origins to meet in one common market. In the market, the
weighted average product properties of the consumption mix can be determined and consistently supplied to the
consumption processes.

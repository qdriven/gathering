# Market Activities

A market activity represents the consumption mix of a product for a given region, accounting for the trade between the
producer and consumer, and, when needed, for product losses that occur during the product’s transportation. A market
dataset does not transform a product but rather simply transfers it from one transforming activity to another.

In the attributional system models (i.e.,
the [cut off system mode](https://ecoinvent.org/the-ecoinvent-database/system-models/#!/allocation-cut-off)l and
the [APOS system model](https://ecoinvent.org/the-ecoinvent-database/system-models/#!/allocation)), markets represent
the average consumption mix of the selected product in the relevant region(s). In
the [consequential system model](https://ecoinvent.org/the-ecoinvent-database/system-models/#!/substitution), a market
represents the marginal consumption mix; it is therefore supplied by unconstrained activities with an up-to-date
technology level.

Market activities for waste (materials for treatment) are defined as treatment mixes rather than consumption mixes. The
market is composed of the different activities that provide a treatment (e.g., landfill, incineration) for the selected
product.

### Regional Definition and Market Groups

Market datasets may refer to a global or local situation. Products that are traded only globally are represented by a
global (GLO) market, while products that are traded locally are available in one or more local markets and often in an
additional [Rest-of-the-World (RoW)](https://ecoinvent.org/the-ecoinvent-database/geographies/#!/global) market.

For example, bananas are traded globally, while heavier materials, such as concrete, are often consumed in the producing
region. Eventual trade with neighbouring countries is modelled with import activities.

#### Imports and exports

[![](https://ecoinvent.org/wp-content/uploads/2021/09/imports-1.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/imports-1-1024x269.png)

A visual representation of an import activity

Import and exports are modelled, where needed, to better represent the regional reality. In the ecoinvent database,
trade between regions is always represented by an import activity.

Hard coal is an example of such a product. Europe receives a substantial portion of its hard coal supply from Australia.
An import dataset transfers hard coal from the Australian market activity for hard coal to the European market activity
for hard coal. The import activity contains data on the amounts of hard coal transferred annually from Australia to
Europe, the average distances and modes of transport required and the product losses occurring during transport, loading
and unloading. The European market activity for hard coal is thus supplied by all activities producing hard coal in
Europe and by all imports from other markets to Europe. Import activities carry the name “… import from X”. For example,
the activity “hard coal, import from Australia” in geography Europe models the transfer of coal from Australia to
Europe.

#### Market groups

A market group is a market dataset exclusively created by market activities that are concerned with the same product but
cover different regions. Therefore, the geography of the market group contains the geography of all supplying markets.
For example, the “market group for electricity, medium voltage” in Europe (RER) bundles markets for medium voltage
electricity in more than 30 countries, including Poland (PL) and Austria (AT).

This feature was introduced in version 3.2 to facilitate readability. Previously, users would see all the individual
European markets supplying electricity to the consumer; now, users see only the “market group for electricity, medium
voltage”/RER.

[![](https://ecoinvent.org/wp-content/uploads/2021/09/electricity-market-group.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/electricity-market-group-1024x595.png)

A visual representation of a market group

### Transport and Product Losses

Market activities account for the average transport distances and modalities of the product from producer to consumer.
Transport information is set by the data provider; when information is not available, default transport assumptions are
used. The global and Swiss default transport assumptions can be downloaded in the report section
of [ecoQuery](https://ecoquery.ecoinvent.org/Account/LogOn). Transport in the market is expressed in tonne-kilometres (
ton\*km) per unit of the reference product. For all products,
the [wet mass property](https://ecoinvent.org/the-ecoinvent-database/properties/#!/product-properties) is used to
calculate the transport values.

Market datasets also account for losses occurring between producers and consumers, when relevant. Losses are modelled
with an input of the product itself to the market, in addition to the amount of product delivered to the consumer. For
example, the consumption of 1 kg of the product “strawberry” in the “market for strawberry” requires the input of 1.1 kg
of the product to the market because 0.1 kg of strawberries are lost, i.e., become biowaste during transportation.

### Direct Links

In the ecoinvent database, markets are the default suppliers for activities in the same geographical area, but this can
be specified differently, using direct links between the producing and consuming activities of a product.

A direct link is set when the supplier is known. In this case, the market dataset is not needed as a bridge between
these producing and consuming activities. Eventual transportation and losses are added directly in the consuming (
transforming) activity in those cases. Direct links are used for services or products that are not traded (i.e.,
immobile infrastructure, intermediate products).

**Example**

Energy-intense industries often own power plants to supply at least part of their own electricity consumption. In these
cases, the industry knows how much of the electricity it consumes is supplied by its own plant and by which technology (
e.g., hydropower).

[![](https://ecoinvent.org/wp-content/uploads/2022/06/activty-link-1-300x171.png)
](https://ecoinvent.org/wp-content/uploads/2022/06/activty-link-1-1024x583.png)

A visual representation direct activity link, i.e. a direct link between the producing and consuming activities of a
product




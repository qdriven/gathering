# Activities & Products

The ecoinvent database is a library of activities representing industrial or agricultural processes, each generating a
resulting product. Each of these activities can also be called a unit process (UPR). More than 18,000 processes covering
around 3,300 distinct products across all economic sectors are included in the latest version of the ecoinvent database.

![img](https://ecoinvent.org/wp-content/uploads/2021/09/activities-300x117.png)

The processes in the ecoinvent database represent the average production conditions within a geographical location,
rather than company-specific or site-specific conditions. For example, the ecoinvent database would contain a process
for the average banana production in Ecuador, rather than for banana production at the farm of a specific fruit company.
Furthermore, the contained products are primarily intermediate products rather than final consumer products. For
example, the database would contain wheat flour but not pasta made from that flour.

## Database Overview

The Database Overview file describes the contents of the database. The following information is contained in the file:

Activity overviews:

- The activity overviews for the undefined data and each of the 4 system models provide a list of all datasets that are
  available in the database for the respective system model. Datasets for specific processes can be searched for by
  activity name or by using the United Nations industry classification system, ISIC (International Standard Industrial
  Classification of All Economic Activities). Additionally, each dataset is assigned to one or more sectors (e.g.,
  Electricity, Wood, Transport, etc), which allows to easily identify processes that belong to the same sector. Datasets
  can also be searched based on the product(s) they produce, either using the product name or based on the CPC (Central
  Product Classification) of the product.
- ecoinvent geographies:
  The geographies used in the ecoinvent database are listed. The type of geography (country, region, etc) is provided,
  as well as information about how the geographies overlap each other.
- LCIA methods:
  The list of all indicators of the life cycle impact assessment (LCIA) methods for which ecoinvent calculates impact
  scores is given. The versions of the methods are provided, as well as information on where to find the documentation
  and original source of the characterization factors of the different methods.

## Activities

Each dataset in the ecoinvent database represents a human activity (process) and its exchanges with the environment and
other human activities.

Each dataset contains information about

- ***its geography***
For example, an activity might be representative of the region of Europe (RER).

- ***its time period***
The time period is described as an interval with a start date and an end date. For example, the dataset ‘nitric acid
production, product in 50% solution state’ has a time period of 2011-2021.
The time period does not represent an expiring date but the period of original data collection or the period to which
the dataset has been extrapolated. A dataset might have an end date that is in the past but is still considered valid
today since production processes or technologies did not change or the supply chain was updated.

- ***its documentation***
The documentation provides a description of what the activity represents, its boundaries, etc.

- ***its natural resource consumption***
For example, the amount of water required to grow 1 kg of cotton.

- ***its emission profile***
For example, the amounts of substances emitted to the atmosphere when combusting 1 kg of coal in a coal power plant.

its material flows in and out of the process, in other words, its bill of materials
For example, the amounts of wood, pulp and various additives needed to produce 1 kg of newspaper.

- ***its energy and fuel consumption***
For example, the amounts and technology mix of electricity used to produce 1 kg of aluminium.

- ***its mass, water, biogenic and fossil carbon accounts***
For example, in a paper production process, how much of the biogenic carbon entering the process in wood inputs ends up
in the paper product versus how much is combusted for energy generation and released as CO2 emissions to the atmosphere.

- ***its annual production volume***
For example, the annual production of hard coal in Australian hard coal mines.

Each activity is uniquely identified based on name, geography and time period: geography is a key factor in
understanding how datasets interact with each other. This unique combination of name, geography, and time period allows
the identification of each undefined dataset by an id number, the so called universal unique identifiers (UUID) number.

## Types of activities

Several types of activities can be distinguished and will be described in more detail below. All activities have
exchanges on the input side and on the output side.

![img](https://ecoinvent.org/wp-content/uploads/2021/09/A-visual-conceptual-representation-of-an-ecoinvent-dataset-1-2048x1239.png)

Exchanges from and to the environment, also called elementary exchanges, are placed on the input side when a process
consumes natural resources, such as iron ore from the ground, water from a river or CO2 taken up from the air into a
tree. Elementary exchanges are placed on the output side when a process releases emissions into soil, water or air.
All other exchanges are intermediate exchanges, i.e., the products consumed or produced by a process and exchanged with
other processes. On the output side, we distinguish between types of products: reference products and by-products or
waste.

### Ordinary transforming activities

All activities that are not of the special types described below are “ordinary” transforming activities. Transforming
activities are human activities that transform inputs so that the output of the activity is different from the inputs,
e.g., a hard coal mine that extracts hard coal in the ground to deliver the marketable product hard coal.

### Treatment activities

Waste in the ecoinvent database has no economic value and is not sold on the market. Since waste are intermediate
exchanges, they cannot be released into the environment; but require treatment processes. Treatment processes (treatment
activities) convert

a waste into a valuable product, e.g., used cooking oil needs to be purified to become a valuable input to biofuel
production. This process can be seen as recycling.
a waste into emissions to the environment, i.e., elementary exchanges. An example would be the treatment of polluted
wastewater to obtain unpolluted water, which is released into a river. This process can be seen as final disposal.
Treatment activities have a negative reference product, e.g., treatment of inert waste in a landfill has a reference
product of -1 kg of inert waste.

The negative sign indicates that the treatment activity supplies the service of treating or disposing of its reference
product. For example, the treatment of unsorted waste paper by sorting has unsorted waste paper as a negative reference
product. Physically, the reference product is an input to the treatment activity, e.g., the unsorted waste paper is an
input to the sorting process. However, reference products in ecoinvent datasets are placed on the output side, and they
have a negative sign to maintain the mass balance of the process. The by-products of the treatment activity have a
positive sign; they represent valuable products obtained after treatment, e.g., the sorted paper leaving the sorting
process.

![img](https://ecoinvent.org/wp-content/uploads/2021/09/treatment-waste-300x118.png)

Dedicated treatment activities often carry the name “treatment of … [name of the product to be treated]”. Treatment or
disposal of a material is their main purpose.

In general, each treatment activity has only one waste as input (negative reference product).

Furthermore, any transforming activity can function as a treatment activity if one of its inputs is a material for
treatment. This case is called speciality production in the ecoinvent database.

### Market activities

![img](https://ecoinvent.org/wp-content/uploads/2021/09/market-2-2048x1029.png)

Market activities are also called market datasets or simply markets. Market datasets transfer the product output of one
or more producing (transforming) activities to activities that consume it as an input, e.g., from hard coal at the
supplier to hard coal at the consumer. The geographical boundaries of a market are chosen to reflect real-world trade
conditions. For example, hard coal consumers in Australia are primarily supplied by hard coal producers in Australia,
justifying an Australian market for hard coal.
Market activities account for transport and losses of the product. They further provide the average consumption mix of a
product for a given region and the marginal consumption mix in the consequential system model.
Learn more about markets here.

### Construction activities

Infrastructure (i.e., capital goods) in the ecoinvent database is defined as products that have a lifetime that exceeds
one year and that are not meant for consumption. This definition includes both stationary infrastructure, such as
buildings, electricity or gas grids, roads, rails, mines and production facilities, and mobile infrastructure, such as
machinery, tools and vehicles.

An activity producing an immobile infrastructure product often carries the term “construction” in its name. Therefore,
these activities are also referred to as construction activities. The reference unit of infrastructure products in the
database is most commonly “unit”, e.g., 1 unit of power plant. A construction activity usually covers the initial
construction, the maintenance of the infrastructure during its lifetime, the land occupation and land transformation (if
applicable) and the decommissioning for waste treatment at the end of the lifetime. The waste streams from
decommissioned infrastructure leave the activity as by-product/waste outputs. The mass of the infrastructure thus leaves
the construction activity with the waste streams; therefore, infrastructure products are an exception in that they do
not come with properties of mass and carbon content.

Instead of mass properties, infrastructure products have properties of “lifetime” and “lifetime capacity”. Read more
about these and other product properties here.

### Service activities

Service activities have inputs and outputs required to perform a service on another product, without the actual input
and output of the product receiving the service. Services are therefore defined as immaterial exchanges, i.e., without a
physical good changing ownership.
For example, the service of sawing with a power saw does not have an input of the tree standing in the forest. Instead,
the forestry process has an input of the tree standing in the forest, an input of power sawing (in hours) and an output
of the felled tree. The amount of the saw, the fuel to operate it, the lubricating oil to maintain it and the emissions
released during operation enter the forestry process indirectly through the service activity.

### Operation activities

Processes with the term “operation” as part of their name represent the use of a specific infrastructure product, e.g.,
“mine operation” as opposed to “mine construction”. Operation datasets thus always have inputs of infrastructure. The
term “operation” is used as a synonym for “use”. The term is applied to both industrial activities, e.g., “gold refinery
operation”, and household activities, e.g., “operation, computer, desktop”. Operation activities may also fulfil the
criteria to be a service activity.
The reference products of operation activities are not of any special type; they are normal products, such as refined
gold resulting from gold refinery operation.

## Products

Every human activity represented in the ecoinvent database has an output of one or more products. These products
comprise materials, goods and services that become available to other human activities, which use them as inputs and
then transform them into yet other products, transfer them to another location, or dispose of them.

The ecoinvent database allows us to follow flows of products within a highly connected network of global supply chains.
Moreover, for every product, the database contains information on

- the environmental impacts associated with its production, transport, trade or disposal. Find out which environmental
  impacts ecoinvent covers here.
- the average price of the product.
- the average physical product properties (for products with mass)
  - Dry mass
  - Wet mass
  - Biogenic and fossil carbon content
- the average consumption mix of a product in a market, i.e., the contribution of different technologies producing the
  same product for a common end market. For example, the shares of electricity produced from hydro, nuclear, coal,
  natural gas and wind in a country.
- trade information: the product average transport modes and distances between the producers and consumers is modelled
  within its market.

## Types of products

### Reference products

The reference product is the driver of a process. It is the product for which a change in demand will affect the
production volume of the process (also known as the determining product). The reference product can be a good or a
service.

### By-products/waste

By-products and waste are co-produced together with the reference product but would not justify performing a process
for their own sake. For example, straw is produced together with wheat grain, which is the reference product.

In most situations, by-products can easily be distinguished from reference products. Often, by-products are similar to
waste and are therefore not even fully utilised, such as straw.

Within the category of by-products/waste, waste does not have an economic value, whereas by-products do have a value on
the market.

The distinction between reference products and by-products/waste is process-specific, i.e., the same product can appear
as a reference product in one process and as a by-product/waste of another process.

Every intermediate exchange also carries two by-product classifications that are consistent across all the processes in
which the exchange appears. These classifications determine the fate of a by-product within the rules of different
system models. You can read more about system models here.
Every intermediate exchange is classified as either waste, recyclable or allocatable product, and every intermediate
exchange is classified either as a material for treatment (mft) or not a material for treatment (non-mft).

# System Models

The system model “Allocation, cut-off by classification”, or the cut-off system model, is based on the recycled content,
or cut-off, approach. In this system model, wastes are the producer’s responsibility (“polluter pays”), and there is an
incentivisation to use recyclable products, that are available burden free (cut-off).

## Introduction to the cut-off system model

The underlying philosophy of this approach is that primary (first) production of materials is always allocated to the
primary user of a material. If a material is recycled, the primary producer does not receive any credit for the
provision of any recyclable materials. As a consequence, recyclable materials are available burden-free to recycling
processes, and secondary (recycled) materials bear only the impacts of the recycling processes. For example, recycled
paper only bears the impacts of waste paper collection and the recycling process of turning waste paper into recycled
paper. It is free of any burdens of the forestry activities and processing required for the primary production of the
paper.

Furthermore, producers of wastes do not receive any credit for recycling or reuse of products resulting from any waste
treatment. For example, heat from the incineration of municipal solid waste can be used to heat houses or offices and
therefore has value. Nevertheless, the incineration is allocated completely to the treatment of the waste; therefore,
the burden is assigned to the waste producer while the heat comes burden-free. This approach to by-product allocation
was also used in ecoinvent versions 1 and 2, where it was the only available system model.

## Classification of products

In the cut-off system model, all intermediate exchanges (i.e., flows from
the [technosphere](https://ecoinvent.org/terminology/)) in the database are classified into one of 3 categories:
allocatable, recyclable or waste. This classification determines how such exchanges will be handled during allocation.
The classification is at the product level, not the individual activity level: throughout the database, an intermediate
exchange can be used and produced many times in many activities, but the classification of each (identified clearly by
name) is consistent throughout the entire database.

A product name may imply a certain category, but classification is not always obvious. For example, waste paper may be
classified as a recyclable material, yet the name contains the term waste for clarity. A full list of all products and
their classifications is available on the ecoinvent website, and the datasets contain classifications of their products.
The classifications are based on the perspective of the data provider and the judgement of the ecoinvent experts and
editors. The choice is made based on the use and fate of the product within the ecoinvent database.

**Allocatable products**

Most goods produced fall into this category. Allocatable products are ordinary (by-)products; they have economic value
and therefore are included in the allocation. Examples of allocatable products include heat and electricity.

**Recyclable materials**

Materials with no or little economic value can serve as the input or resource for a recycling activity; therefore,
interest in their collection exists. Examples include metal scraps and waste paper.

**Waste products**

Waste products are materials with no economic value and no interest in their collection without compensation. The
producer therefore generally has to pay to dispose of these materials; thus, he consumes the service of disposing of
these materials. Examples are wastewater, chemically polluted soil and radioactive waste.

## Handling of by-products by classification

The cut-off system model has, broadly speaking, the effect that recyclable materials are cut off at the beginning of the
treatment processes, becoming available burden-free for following uses. The treatment of waste is completely allocated
to the waste producer, and all valuable by-products of waste treatment are cut off in the waste treatment and become
available burden-free. Ordinary by-products are handled by allocation among products if an activity produces more than
one product.

The following sections describe in more detail what happens to by-products in this system model.

**Handling of waste products**

Waste by-products have to be treated, and the treatment burden is allocated completely to the waste-producing activity.
Therefore, wastes are linked as a negative input to the activity, representing the fact that the activity requires the
service of waste disposal. Waste disposal is then provided by different treatment processes, which have inputs and
emissions that add to the burden of the waste-producing activity.

Any non-waste by-products of a waste treatment process (i.e., not other waste products) are cut off and do not provide
credit to the production activity. The cut-off point is therefore the end of the waste treatment, which means that the
resulting products are available in the database and can be used as burden-free inputs in other activities.

**Handling of recyclable materials**

Recyclable materials are cut off from their production activities through the use of special datasets, denoted as
“product name, recycled content cut-off”. These datasets have no inputs or emissions and are therefore burden-free. In a
production activity, the material is recorded as a negative input, as in the case of waste; however, the material is not
linked to any treatment activity but simply to the empty process.

Thus, the cut-off approach is simple on the producing side. The cut-off point is at the end of the activity producing
the recyclable material. The secondary use cycle begins with pick-up of the material from the producer, and transport to
the processing site is the beginning of the supply chain for the secondary use. In the system model, a process
requesting a recyclable material as an input, e.g., a recycling process, receives the product from its market, which
links to the burden-free recycled content cut-off dataset.

**Special case: recycling chains**

Recycling processes can occur over several linked unit processes. Often, the cut-off simply occurs at the beginning.
However, recycling products are sometimes produced in different forms during a recycling process. This case is best
explained with an example. Waste glass is first treated by processing it and breaking it down into glass cullets, which
are recyclable materials that can be turned into glass bottles. In this example, both waste glass and glass cullets are
considered recyclable materials, so other producers producing either of them will have these by-products cut off. For
recycling, however, the system model maintains the recycling chain, so glass cullets will have a non-empty supply chain
despite being a recyclable material. The glass cullet supply chain will lead all the way to the beginning of the
secondary use cycle, with the collection of waste glass, and there is no cut-off between waste glass and glass cullets.

**Handling of allocatable products**

After the handling of waste and recyclable materials, allocation occurs for all remaining allocatable by-products
produced within the activity. This process uses the allocation factors defined in the dataset by the dataset author. As
waste and most recyclable materials (except those within recycling chains, where they remain as products) are at this
point moved to the input side of the activity, they will be considered similar to other inputs and allocated over the
different co-products of the activity.

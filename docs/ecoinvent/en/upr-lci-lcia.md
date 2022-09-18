# UPR,LCI,LCIA

### Unit Process (UPR)

The basic building blocks of the database are individual processes of human activities and their exchanges with the
environment (elementary exchanges) and with the technosphere (intermediate exchanges).

[![](https://ecoinvent.org/wp-content/uploads/2021/09/UPR-1-1024x317.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/UPR-1-1024x317.png)

In the ecoinvent database, these are called unit processes (UPR), also known as gate-to-gate inventories. These
processes are neither vertically aggregated with subsequent processes in a supply chain nor horizontally aggregated with
processes delivering the same intermediate outputs. Hence, every process that occurs along a supply chain forms its own
unit, for which a separate life cycle inventory is available.

Nevertheless, activities are most often reported at the national level, averaging information from different producers
using the same technology in the same country to deliver meaningful background data to the user. Similarly, UPR would
rarely represent the production of products that are exclusively used as intermediate products for a subsequent process.

**Undefined and linked UPR**

UPRs are available in undefined and linked forms. Undefined unit processes show the data as compiled by the data
provider. Undefined UPRs are unlinked (no suppliers determined) multi-product (multi-output) activities. This is the
starting point on which system model-specific modelling choices are applied. The supply chain is determined (linking),
and subdivision and allocation or substitution are applied to produce single-product UPRs (see system models section).

**Note**: in [ecoQuery](https://ecoquery.ecoinvent.org/Account/LogOn), you can access both forms of UPR simply by
selecting either “undefined” or the “system model of your choice”. Undefined UPRs are also accessible as a guest user,
while linked unit processes, LCI and LCIA are available only to licensees.

### Cumulative Life Cycle Inventory (LCI)

In order to generate value chains and calculate environmental impacts of products, the individual UPRs are linked into
supply chains (systems).

[![](https://ecoinvent.org/wp-content/uploads/2021/09/unit-process.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/unit-process-1024x398.png)

[![](https://ecoinvent.org/wp-content/uploads/2021/09/unit-process-2-1.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/unit-process-2-1-1024x471.png)

Where natural resource consumption or emissions of the same type occur at different stages of a supply chain, their
amounts are aggregated. This results in a comprehensive list of the natural resources taken from and the emissions
released to the environment associated with the life cycle of the final product, from cradle to the factory gate. Where
end-of-life treatment or disposal processes of wastes are required, the life cycle ranges from cradle to grave.

The aggregated list of elementary exchanges associated with the life cycle of a product is called the cumulative life
cycle inventory (LCI).

[![](https://ecoinvent.org/wp-content/uploads/2021/09/LCI-1.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/LCI-1-1024x471.png)

### Life Cycle Impact Assessment (LCIA)

The cumulative list of elementary exchanges does not yet provide information about the environmental impact caused by
these natural resource inputs and emissions to the environment.

This is where [Life Cycle Impact Assessment](https://ecoinvent.org/the-ecoinvent-database/impact-assessment/) (LCIA)
methods come into play. They quantify what and how much damage or benefit is associated with an elementary exchange in
the form of so-called characterisation factors (CFs). For example, methane (CH4) is a greenhouse gas that has an impact
on climate change measured as global warming potential in kg CO2-equivalent (CO2-eq). The impact assessment considers
that the effects of methane in the atmosphere are 29 times higher as those of CO2 when it comes to global warming.
Therefore, the emission of 1 kg of CH4 is multiplied by the CF of 29, resulting in a global warming potential of 29 kg
CO2-equivalents.

[![](https://ecoinvent.org/wp-content/uploads/2021/09/LCI-2.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/LCI-2-1024x536.png)

Elementary exchanges may contribute to one or
more [impact categories](https://ecoinvent.org/the-ecoinvent-database/impact-assessment/), such as “climate change”,
“human toxicity”, “land use”, or “water use”. Once all exchanges have been matched and multiplied with all their CFs,
the result is the LCIA score of a product.

[![](https://ecoinvent.org/wp-content/uploads/2021/09/LCIA-1.png)
](https://ecoinvent.org/wp-content/uploads/2021/09/LCIA-1-1024x557.png)

As a background database, the focus is on the compilation of the basic building blocks, UPRs, representing the
individual unit processes of human activities and their exchanges with the environment, and the combination of these
UPRs in supply chains to form LCIs. Nevertheless, the database also contains data on LCIA scores. These are calculated
by applying already developed LCIA methods, such as the global warming potential of the Intergovernmental Panel on
Climate Change (IPCC).

Download the LCIA implementation file in the file section of [ecoQuery](https://ecoquery.ecoinvent.org/Account/LogOn) to
see what LCIA methods are available in the ecoinvent database and which CFs apply.

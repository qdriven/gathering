7      Good practice for documentation


7.1      Detail of documentation
The data used to describe the exchanges of a particular activity are discussed within the context of values from various sources. Values are generally not supplied without comment.
Comments and references to sources (see Chapter 7.5) are given on the most detailed level possible (i.e. attributed to the particular exchanges of an activity, attributed to a particular property of an ex- change, if possible and relevant), describing the individual values and their estimation. Comments and references that are general to more than one entry are provided in the comment field most relevant for the nature of the value. The “technology comment” field is used for comments and references general to the specific technology and the "general comment" field for comments and references of more gen- eral nature that cannot be placed in any of the more specific comment fields.
In general, the information in the dataset should be sufficient to judge the appropriateness of a dataset for a specific application. Background information that is common for many datasets are available on www.ecoinvent.org under the web-page for the ISIC activity class in question (see Chapter 9.7) or sub-pages to this, as indicated in the "general comment" field of the dataset.
Additional advice for data providers:
Information that is required to judge the appropriateness of a specific dataset for a specific application shall be placed in the dataset. The web-pages only contain less essential background information common to several da- tasets. This implies e.g. that the dataset should not contain references such as “For exceptions, see [web-page]” .
[Changes relative to ecoinvent version 2: The content of the reports from version 2 are placed partly in the datasets, partly on web-pages with the same structure as the ISIC activity classification. Web- pages will also be available for methodological issues, structured in the same way as this data quality guideline. In some ecoinvent v2 datasets, the General comment field contains redundant information that should be removed when updating, for example: “Inventory refers to the production of 1 kg …” , which is already given in the exchange information for the reference product.]

7.2      Images
Images may be included in any of the “TextAndImage” fields of a dataset and additionally a Dataset Icon may be available, serving as a quick identification of the specific dataset (may also be used for product brands and company logos).

7.3      Copyright
ecoSpold reference: isCopyrightProtected (field 3540)
When supplying a dataset to the ecoinvent database, the data provider confirms that the data are free from prior copyright, and makes a non-exclusive transfer of the right of use to the ecoinvent Centre.
In general, all ecoinvent datasets are subject to copyright. However, with the assistance of sponsors it has become possible for some ecoinvent datasets to be provided as open access datasets, which can be freely shared, see Chapter 7.4.4. Use of these open access datasets is still subject to the normal rules for citation.




7.4     Authorship and acknowledgements

7.4.1    Commissioner
The ecoSpold data format does not have a separate field for information on the commissioner for a specific dataset, i.e. the person or organisation paying for the data collection.
When such information is available, it is placed in the General comment field, which may refer to an entry in a Person field (can also be used for organisations).

7.4.2     Data generator
The data generator is the person or organisation that collected, compiled or published the original da-
ta. This may or may not be the same person as the author (see 'DataEntryBy'; Chapter7.4.3).
The intention of this field is to acknowledge and reference the origin of the data and the person or or- ganisation that performed the majority of the work in data collection. Minor changes and adjustments by subsequent authors do not make these persons data generators, unless this involves a new publica- tion of the entire dataset in a context outside the ecoinvent database.

7.4.3    Author (Data entry by)
The field dataEntryBy refers to the author of the dataset, i.e. the person that entered data into the da- tabase format and provided it to ecoinvent and thereby is the person responsible for the data. The da- taset author may or may not be different from the data generator; see Chapter7.4.2. The author may make minor modifications or adjustments to the datasets to fit the data to the ecoinvent requirements, without this implying that the author then also is the data generator.
Authors are subject to authorisation by the ecoinvent database administrator before being allowed to upload datasets to the ecoinvent validation and review procedure. The uploaded data are automatically stamped with the identity of the author. As part of the submission procedure, the author confirms that the data are free from prior copyright and makes a non-exclusive transfer of the right of use to the ecoinvent Centre, see Chapter 7.3. For modifications to datasets with an active author, see Chapter 16.3, the review procedure includes a request to the active author for the right to perform the modifi- cations. The original author may then decide to perform the extrapolation and thereby maintain au- thorship also to the extrapolated dataset. If creating a new dataset, e.g. an update, which is largely an
extrapolation from an existing dataset, it is good practise for the new data provider to seek permission from the original author.

7.4.4    Open access sponsors
A part of the ecoinvent database is made freely available to the public. The free public access to the datasets in this part of the ecoinvent database is made possible through sponsorships. The sponsored datasets are free of copyright (see Chapter 7.3), but are subject to the normal rules for citation (see
Chapter15.5).
The sponsored datasets are labelled with the following sentence in the general comment field: “The kind contribution of [sponsor name] has made it possible to make this dataset freely available to the public. The sponsors have no influence on the content and/or validation procedure for the sponsored datasets.”



Datasets are made freely available for a minimum period of 3 years. The sponsored datasets stays in the free part of the database also after the termination of the 3-year period. Any later updates (i.e. im- provements made after the 3-year period or new versions of the same dataset for later years) will only be made freely available if a new sponsorship agreement is made.
The ecoinvent Centre retains the right to refuse sponsors without stating any reason for this refusal.
Technical disclaimer: If parent/child relationships between datasets applies (e.g. the same dataset for several countries), the sponsorship applies either to the parent dataset alone, or to one specific in- stance of a child dataset.

7.5      Referencing sources
Source references are centrally collected and managed in a master file for the entire ecoinvent data- base.
When the source is not a scientific article, book-chapter or separate publication, the title field is re- used to refer to e.g. "Measurement documentation of company XY" (for measurements on site), "Oral communication, company XY" or "Personal written communication, Mr./Mrs. XY, company Z". Cita- tions of large reference works include chapter numbers, table numbers and/or page numbers.
[Changes relative to ecoinvent version 2: References to sources are now placed directly in each da- taset, and data sources are publicly available, preferably in the master file for sources. For datasets transferred from ecoinvent version 2, the sources may not all be transferred to the master file for sources but may temporarily be placed as free text, either in the dataset or on a referenced web-site (for sources used for many datasets).]

7.6     Version management
The ecoSpold format defines two version numbers for each dataset: Release and Revision, each with a major and minor component.
The release number defines the version of the ecoinvent database that the dataset is part of. A new re- lease number is only entered by the database administrator when a new production database is created in preparation of the next official release (see Chapter 3). Both the major and minor release compo-
nent can be changed when a new database is created. All datasets of one database must have the same release number and once this is entered on database creation it is not changed later on.
The revision number is specific to each dataset and is independent of the overall database release ver- sion. The major revision component reflects the amount of accepted changes to the dataset. It is in- creased automatically by the database software when changes to the dataset have been accepted by the ecoinvent review procedure and the revised dataset is uploaded to the production database. It will only increase over time and must not be changed manually. The minor revision component describes ver- sions of the dataset during the editing process before it is submitted for review. It is increased auto- matically by the ecoEditor software every time the data provider saves changes made to the dataset either locally or as a draft on the ecoinvent server. The minor revision component is reset to “1” each time the major revision component is increased (when changes to a dataset are accepted by a review- er).
The revision number may also be used to notice concurrent editing of the same dataset by two data providers. If two data providers request the same dataset for editing, one will finish the editing before the other. If the reviewer accepted the changes of the first data provider, the major revision compo- nent will have increased by the time the second data provider submits changes for review. The review process must then reject the second changes because they are not based on the current version of the



dataset. The data provider would have to request the current version of the dataset for editing and en- ter the necessary changes again.
[Changes relative to ecoinvent version 2: The version management is more stringent and automati- cally controlled than in version 2.]

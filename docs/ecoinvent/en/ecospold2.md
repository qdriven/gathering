.dt-breadcrumbs-id-7dea592d0311fcb4f4c7b8a9f7f2ac31 .breadcrumbs { display: inline-block; margin: 0; padding: 2px 10px
2px 0px; border: 0px solid ; border-radius: 0px; } .dt-breadcrumbs-id-7dea592d0311fcb4f4c7b8a9f7f2ac31 .breadcrumbs \* {
color: #a2a5a6; }

You are here:

1. [Home](https://ecoinvent.org/ "Home")
2. [ecoinvent Database](https://ecoinvent.org/the-ecoinvent-database/ "ecoinvent Database")
3. [Data Formats](https://ecoinvent.org/the-ecoinvent-database/data-formats/ "Data Formats")
4. ecoSpold2

ecoSpold2
=========

### The ecoSpold2 format is used to create life cycle inventories for ecoinvent version 3. This format sets up standards on what are mandatory and what are optional fields for a standard life cycle inventory.

The ecoSpold2 format replaces the ecoSpold1 format for ecoinvent version 3 released in May 2013. New developments in the
field of LCA software demanded a revision of the data format. An ad-hoc expert working group was formed by ecoinvent to
guide the revision process and an open hearing has been conducted among users of the ecoSpold format. The result of this
hearing and the way the input has been treated can be seen
in [this public report](https://ecoinvent.org/wp-content/uploads/2021/09/200905_ecospold1_open_hearing_feedback_with_comments_on_implementation_in_v2.pdf)
. The final ecospold2 format is designed to represent all three stages of life cycle assessment: UPR, LCI and LCIA on an
xml basis.

Among others, the ecospold2 format adds features such as:

* Properties of exchanges like dry mass, wet mass, carbon content etc.
* Mathematical relations in a
  new [formula language](https://ecoinvent.org/wp-content/uploads/2020/10/ecospold02_formula_language_specification.pdf)
  and variable names for exchanges, properties and parameters
* Use of UUIDs for referencing certain fields
* New fields for production volumes

For a comparison between ecospold1 and ecospold2
visit: [Changes ecospold1 to ecospold2](https://ecoinvent.org/the-ecoinvent-database/data-formats/changes-ecospold1-to-ecospold2/)

Today, ecospold2 is used by most of
the [software providers](https://ecoinvent.org/the-ecoinvent-association/software-tools/) that use the ecoinvent
database. The open-source python framework [Brightway2](https://2.docs.brightway.dev/) supports the import of ecospold2
as well.

### Supporting Files & Documents

#### **[Documentation on ecoSpold2 format \[zip\]](/wp-content/uploads/2020/10/documentation_on_ecospold2_format.v1.0.13.zip "documentation_on_ecospold2_format.v1.0.13")**

This zip file contains the following files describing datasets and master data files:

* schema definition (xsd)
* stylesheets (xsl)
* user-friendly description of the formats (html)

* * *

#### **[ecoinvent geography definitions](http://geography.ecoinvent.org/)**

This webpage describes the creation and processing of geodata for the ecoinvent database.

* * *

#### **[ecoEditor User Manual \[pdf\]](/wp-content/uploads/2020/10/ecoeditor_introduction_20130503-1.pdf)**

A short introduction to the ecoEditor for ecoinvent v3

* * *

#### **[Dataset Documentation Manual \[pdf\]](/wp-content/uploads/2020/10/dataset_documentation_ecoinvent_3.pdf "Manual - Dataset Documentation")**

This document assists in the proper documentation of datasets explaining the requirements and expectations for these
fields.

* * *

#### **[Formula Language Specification \[pdf\]](/wp-content/uploads/2020/10/ecospold02_formula_language_specification.pdf "ecoSpold2 Formula Language Specification")**

The ecoSpold2 format introduces the new field “mathematicalRelation” for exchanges, properties and parameters. The
allowed content for this field is described in this document.

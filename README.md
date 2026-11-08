# UniAid — Community Service

UniAid is an Odoo add-on for managing university community service projects, student volunteers, supporting organizations, and contractors. It provides project planning and reporting tools alongside volunteer hour tracking and certificates of appreciation.

## Group Members

- Ezhilarunan
- Vishnu
- Shreyaas
- Soham
- Harshini

## Features

- **Projects:** Track project descriptions, dates, status (Planning, Ongoing, or Completed), expenses, donor organizations, and a primary contractor. View projects in kanban, list, form, graph, and calendar views.
- **Volunteer records:** Maintain student contact details, university IDs, majors, and registration indicators for Sharjah Social Services and Emirates Red Crescent.
- **Volunteer hours:** Record student hours against projects. A volunteer’s total is calculated from projects marked Completed.
- **Certificates:** Generate a PDF Certificate of Appreciation from a volunteer record. The form also offers an email action that sends the certificate using the configured mail template.
- **Donor organizations:** Record organization type, pledged and donated amounts, university contact, and supported projects. Donation progress is displayed as a percentage.
- **Contractors:** Keep contractor contact information and see expenses summed across their projects.
- **Project progress PDF:** Print a report with project status and dates, donors, contractor, expenses, volunteer hours, and notes.

## Requirements

- Odoo 19.0
- Odoo modules `base` and `mail` (both are declared dependencies)

## Installation

1. Place the `community_service` directory in an Odoo add-ons directory. In this repository it is under `workshop/Workshop/community_service`; add `workshop/Workshop` to Odoo’s `addons_path`.
2. Restart Odoo and update the Apps list from the Apps screen (enable developer mode if the update option is hidden).
3. Search for **UniAid** and install it.
4. Open the **UniAid** app and use Projects, Volunteers, Organizations, or Contractors from the menu.

For a command-line installation, start Odoo with the appropriate database and add-on path, then update/install the module, for example:

```bash
python odoo-bin -d <database> -i community_service --stop-after-init --addons-path=<odoo-addons-path>,<path-to-workshop/Workshop>
```

Replace the placeholders with paths and a database name for your environment. If Odoo is already running, restart it after installing or updating the module.

## Usage notes

1. Create volunteer, donor organization, and contractor records as needed.
2. Create a project, set its dates and status, then add volunteer rows with hours. Select any supporting organizations and contractor.
3. Mark projects **Completed** for their logged hours to count toward volunteer totals and certificates.
4. Use the report actions on a project or volunteer record to print PDFs. From a volunteer form, **Send Certificate by Email** sends the attached certificate to the saved email address; configure outgoing mail in Odoo first.

## Access

The module grants Odoo internal users (`base.group_user`) read, create, write, and delete access to its volunteer, project, project volunteer log, organization, and contractor records. Access should be restricted through your Odoo user and database configuration as appropriate.

## Technical information

- **Technical module name:** `community_service`
- **Odoo app name:** UniAid
- **Models:** `csr.project`, `csr.project.volunteer.line`, `csr.volunteer`, `csr.fundraising`, and `csr.contractor`
- **Dependencies:** `base`, `mail`
- **Demo data:** `data/demo_data.xml`
- **Backend assets:** custom SCSS theme and navigation styling


import unittest

import api

from patient_entry import PatientEntry
from add_order import OrderEntry 
from modify_order import ModifyOrder 
from work_plans import WorkPlans
from non_conformity import NonConformity
from results_entry import ResultsEntry
from referral_out import ReferralOut
from validation import Validation
from reports import Reports
from patient_report import PatientReport
from permission import Permission
from config_items import ConfigItems
from modifier_echantillon import ModifierEchantillon
from rename_test_sections import RenamTestSections 
from rename_existing_measure import RenamExistingMeasure
from ajouter_nouveaux_tests import AjouterNouveauxTests
from gerer_unites_tests import GererUnitesTests
from gestion_types import GestionTypes
from manage_panels import ManagePanels
from ordonnances import Ordonnances
from test_management import TestManagment






def main():
    all_sheets = [
                PatientEntry,
		OrderEntry, 
		ModifyOrder, 
		WorkPlans,
		NonConformity,
		ResultsEntry,
		ReferralOut,
		Validation,
		Reports,
		PatientReport,
		Permission,
		ConfigItems,
		ModifierEchantillon,
		RenamTestSections, 
		RenamExistingMeasure,
		AjouterNouveauxTests,
		GererUnitesTests,
		GestionTypes,
		ManagePanels,
		Ordonnances,
		TestManagment,
    ]
    for Sheet in all_sheets:
        suite = unittest.TestLoader().loadTestsFromTestCase(Sheet)
        unittest.TextTestRunner(verbosity=2).run(suite)

    api.reporter.display_report()


if __name__ == '__main__':
    main()

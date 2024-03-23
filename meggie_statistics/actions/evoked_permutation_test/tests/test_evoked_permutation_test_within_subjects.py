from meggie_statistics.utilities.testing import BaseStatisticsTestAction
from meggie_statistics.actions.evoked_permutation_test import PermutationTest
from meggie_statistics.utilities.dialogs.permutationTestDialogMain import (
    PermutationTestDialog,
)


class TestEvokedPermutationTest(BaseStatisticsTestAction):
    def test_evoked_permutation_test(self):

        data = {"outputs": {"evoked": ["Evoked"]}}

        self.run_action(
            action_name="evoked_permutation_test",
            handler=PermutationTest,
            data=data,
            patch_paths=["meggie_statistics.actions.evoked_permutation_test"],
        )
        dialog = self.find_dialog(PermutationTestDialog)

        dialog.ui.radioButtonWithinSubjects.setChecked(True)
        dialog.groups = {
            "1": [
                "sample_01-raw",
                "sample_02-raw",
                "sample_03-raw",
                "sample_04-raw",
                "sample_05-raw",
            ],
            "2": [
                "sample_06-raw",
                "sample_07-raw",
                "sample_08-raw",
                "sample_09-raw",
                "sample_10-raw",
            ],
        }
        dialog.accept()

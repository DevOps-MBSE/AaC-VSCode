from unittest import TestCase
from typing import Tuple
from click.testing import CliRunner
from aac.execute.command_line import cli, initialize_cli
from aac.execute.aac_execution_result import ExecutionStatus


from aac_vscode.plugins.lsp_server.lsp_server_impl import (
    plugin_name,
    start_lsp_io,
    start_lsp_tcp,
)


class TestLSPServer(TestCase):
    def test_start_lsp_io(self):
        # TODO: Write unit tests for start_lsp_io
        self.fail("Test not yet implemented.")

    def run_start_lsp_io_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["start-lsp-io"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_start_lsp_io(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_start_lsp_io_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

    def test_start_lsp_tcp(self):
        # TODO: Write unit tests for start_lsp_tcp
        self.fail("Test not yet implemented.")

    def run_start_lsp_tcp_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["start-lsp-tcp"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_start_lsp_tcp(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_start_lsp_tcp_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.


Feature: Ensure the LSP server starts in IO mode.

  Scenario: Start the LSP server in IO mode.
  
      Given The LSP server is not currently running.
      When The aac application is run with the start-lsp-io command.
      Then The aac application is run with the start-lsp-io command.
      
    
  
  
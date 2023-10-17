"""Module for the Hover Provider which handles all hover requests."""

from typing import Optional

from pygls.lsp.types import MarkupContent, MarkupKind, Hover, HoverParams
from pygls.server import LanguageServer
from pygls.workspace import Document

from aac_vscode.plugins.lsp_server.providers.symbols import get_symbol_at_position
from aac_vscode.plugins.lsp_server.providers.lsp_provider import LspProvider

# TODO:  I cleaned up the imports for AaC 0.4.0, but still need to fix the code below.

class HoverProvider(LspProvider):
    """Provide useful contextual information for the named item being hovered over."""

    def handle_request(self, language_server: LanguageServer, params: HoverParams) -> Optional[Hover]:
        """Return the YAML representation of the item at the specified position."""
        document: Optional[Document] = language_server.workspace.documents.get(params.text_document.uri)

        return_hover = None
        if document:
            position = params.position
            symbol = get_symbol_at_position(document.source, position.line, position.character)

            if symbol is not None:
                name = remove_list_type_indicator(symbol).strip(":")
                definition = language_server.language_context.get_definition_by_name(name)

                if definition:
                    return_hover = Hover(
                        contents=MarkupContent(kind=MarkupKind.Markdown, value=f"```\n{definition.content}\n```")
                    )

        return return_hover

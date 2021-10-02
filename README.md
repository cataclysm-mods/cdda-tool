# CDDA Tool

This project is a wrapper around a variety of Python code written by the broader development community around Cataclysm: Dark Days Ahead.

## Design Goals

* Provide a common interface for auxillary tooling related to Cataclysm: Dark Days Ahead
* Provide a common package and distribution available via PIP that may be used to distribute these tools independently from Cataclysm's game distribution
* Attempt to formalize behavior and functionality of these tools with tests and documentation covering their behavior

## Dependencies

At the time of this writing, many dependencies for the python code used by developers of CDDA are implicit and not exhaustively documented. This project makes an effort to explicitly define and document such dependencies as they are encountered.

### Cataclysm GFX tools

* https://github.com/I-am-Erk/CDDA-Tilesets/tree/master/tools
* https://github.com/CleverRaven/Cataclysm-DDA/tree/master/tools/gfx_tools

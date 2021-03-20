# sdr_trunk_alias_import

This is a Crude Python script to export a csv file with alias into XML so you can import it into SDR-Trunk


Make sure SDR-Trunk is not running

Step 1) Add data to import.csv in the same format as example

Step 2) run ``python convert.py``

Step 3) open ``alias.xml`` in your fav editor

Step 4) Copy all the content in alias.xml

Step 5) open ``default.xml`` in your SDR-Trunk Playlist folder in your fav editor.

Step 6) Goto bottom of ``default.xml`` file just before ``<\playlist>``

Step 7) Paste data into ``default.xml``

Step 8) save ``default.xml``

Job Done!!!

Open SDR-Trunk and check ``Aliases`` Tab

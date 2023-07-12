# Color-Scheduler
Requested by: Nathan Garcia & Hope Griffin
Developed by: Joel Villamor
V: 1.0.0

Abstract:
The color scheduler was meant to tackle the irritably tedious process of counting,  
reordering, and verifying order color plans. As a manual process, this task usually 
cost its users anywhere from 45 mins to 2+ hrs. The result of this software is producing the same color plans at a fraction of the time spent as the production of these lists are usually instantaneous. 


Inputs/Outputs:
The color scheduler, takes truck closing data (csv) and a corresponding color sequence.
The color sequence is a csv document formatted within the first column. The original 
Brentwood color sequence will provide the order in which the colors are handled. 

1. color sequence

By taking this data and formatting it within one column (one color per row), the software
takes it and creates an inner dictionary (the order being preserved). The dictionary 
entries are incremented per color as the truck closing file is being evaluated. This
creates the corresponding quantities seen in the table after clicking "Visualize".

2. truck closing file

After clicking "Save", the color scheduler will prompt the user with a file saving
prompt. This software produces a csv formatted file and it is preferable that the user
place the '.csv' extension at the end of the desired filename, though it is not necessary to see the data.

Output: <filename>.csv

<Note:>
The output of the software will first be the colors that followed the algorithm and are sorted correctly. The additional field, preficed with "Unmatched Colors:" are colors and their corresponding quantities that did not match the input color sequence.

These colors will have to be manually sorted within the correctly sorted entries above. These unmatched colors likely signify that the inputted "color sequence" file 
is outdated and in need of updating.  

Bug Report/Feedback form:
https://forms.office.com/Pages/DesignPageV2.aspx?origin=NeoPortalPage&subpage=design&id=b6WNC91KR0a8VR2kwHD_ASsGFTGswvFOin0cLP8glVhUM1lWTFBEMENETktVRUE3VU8yNTlWNUU4RC4u&topview=Preview

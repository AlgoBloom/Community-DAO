# How do we use one global variable to represent a vote and a count?
# I think in this case I need to use a global integer to represent the count of each vote
# do we need local state for anything? I dont think so

from pyteal import *

on_creation = Seq(
    # Global byteslice 1
    App.globalPut(Bytes("App_Name"), Bytes("Community 1 Voting Application")),
    # Global byteslice 2
    App.globalPut(Bytes("A_Description"), Bytes("Details for option A.")),
    # Global byteslice 3
    App.globalPut(Bytes("B_Description"), Bytes("Details for option B.")),
    # Global byteslice 4
    App.globalPut(Bytes("C_Description"), Bytes("Details for option C.")),
    # Global byteslice 5
    App.globalPut(Bytes("D_Description"), Bytes("Details for option D.")),
    # Global int 1
    App.globalPut(Bytes("A_Count"), Int(0)),
    # Global int 2
    App.globalPut(Bytes("B_Count"), Int(0)),
    # Global int 3
    App.globalPut(Bytes("C_Count"), Int(0)),
    # Global int 4
    App.globalPut(Bytes("D_Count"), Int(0)),
    # Approves sequence
    Return(Int(1))
)
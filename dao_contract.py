# How do we use one global variable to represent a vote and a count?
# I think in this case I need to use a global integer to represent the count of each vote

from pyteal import *

on_creation = Seq(
    # Global byteslice 1
    App.globalPut(Bytes("App_Name"), Bytes("Community 1 Voting Application")),
    # Global byteslice 2
    App.globalPut(Bytes("Option A"), Bytes("Details for option A.")),
    # Global byteslice 3
    App.globalPut(Bytes("Option A"), Bytes("Details for option A.")),
    # Global byteslice 4
    App.globalPut(Bytes("Option A"), Bytes("Details for option A.")),
    # Global byteslice 5
    App.globalPut(Bytes("Option A"), Bytes("Details for option A.")),
    # Global int 1
    App.globalPut(Bytes("A_Count"), Int(0)),
    
)
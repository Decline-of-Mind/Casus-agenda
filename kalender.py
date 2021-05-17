import sys



# Afspraakmoment hardcoded, normaal gezien vanuit database/calendar module
agenda = {  1:{ "naam" : "Maandag", "tijdslot" : {
                                            1: {"tijd": "9:00-10:00", "bezet": True },
                                            2: {"tijd": "10:15-11:15", "bezet": True },
                                            3: {"tijd": "11:30-12:30",  "bezet": True },
                                            4: {"tijd": "13:15-14:15",  "bezet": True },
                                            5: {"tijd": "14:30-15:30",  "bezet": True },
                                        }
                        },
            2:{ "naam" : "Dinsdag", "tijdslot" : {
                                            1: {"tijd": "9:00-10:00", "bezet": True },
                                            2: {"tijd": "10:15-11:15", "bezet": True },
                                            3: {"tijd": "11:30-12:30",  "bezet": True },
                                            4: {"tijd": "13:15-14:15",  "bezet": False },
                                            5: {"tijd": "14:30-15:30",  "bezet": True },
                                        }
                        },
            3:{ "naam" : "Woensdag", "tijdslot" : {
                                            1: {"tijd": "9:00-10:00", "bezet": False },
                                            2: {"tijd": "10:15-11:15", "bezet": True },
                                            3: {"tijd": "11:30-12:30",  "bezet": True },
                                            4: {"tijd": "13:15-14:15",  "bezet": False },
                                            5: {"tijd": "14:30-15:30",  "bezet": True },
                                        }
                        },
            4:{ "naam" : "Donderdag", "tijdslot" : {
                                            1: {"tijd": "9:00-10:00", "bezet": True },
                                            2: {"tijd": "10:15-11:15", "bezet": True },
                                            3: {"tijd": "11:30-12:30",  "bezet": True },
                                            4: {"tijd": "13:15-14:15",  "bezet": False },
                                            5: {"tijd": "14:30-15:30",  "bezet": True },
                                        }
                        },
            5:{ "naam" : "Vrijdag", "tijdslot" : {
                                            1: {"tijd": "9:00-10:00", "bezet": True },
                                            2: {"tijd": "10:15-11:15", "bezet": False },
                                            3: {"tijd": "11:30-12:30",  "bezet": True },
                                            4: {"tijd": "13:15-14:15",  "bezet": False },
                                            5: {"tijd": "14:30-15:30",  "bezet": True },
                                        }
                        },
    }
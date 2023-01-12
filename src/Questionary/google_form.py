from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": "RoboAdvisor 1.1",
    }
}

# Request body to add a multiple-choice question
NEW_QUESTION = {
    "requests": [{"createItem": {
            "item": {
                "title": "What is your goal for investing?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "prepare for retirement."},
                                {"value": "save for major upcoming expenses (education, health bills, etc.)."},
                                {"value": "save for something special (vacation, new car, etc.)."},
                                {"value": "build a rainy day fund for emergencies."},
                                {"value": "generate income for expenses."},
                                {"value": "build long term wealth."},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 0
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 2",
                "pageBreakItem": {},
            },
            "location": {
                "index": 1
            }
        }
    }, {"createItem": {
            "item": {
                "title": "What is your understanding of stocks, bonds, and ETFs?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "None"},
                                {"value": "Good"},
                                {"value": "Some"},
                                {"value": "Extensive"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 2
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 3",
                "pageBreakItem": {},
            },
            "location": {
                "index": 3
            }
        }
    }, {"createItem": {
            "item": {
                "title": "When you hear “risk” related to your finances, what is the first thought that comes to mind?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "I worry I could be left with nothing."},
                                {"value": "I understand that it’s an inherent part of the investing process."},
                                {"value": "I see opportunity for great returns."},
                                {"value": "I think of the thrill of investing."},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 4
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 4",
                "pageBreakItem": {},
            },
            "location": {
                "index": 5
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Have you ever experienced a 20% or more decline in the value of your investments in one year?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "Yes"}, #"goToSectionId": "6cfbb743"}, 
                                {"value": "No"}, #"goToSectionId": "286df58d"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 6
            }
        }
    }, {"createItem": {
            "item": {
                "itemId": "6cfbb743",
                "title": "Question 5a",
                "pageBreakItem": {},
            },
            "location": {
                "index": 7
            }
        }
    }, {"createItem": {
            "item": {
                "title": "What did you do when you experienced a 20% decline in the value of your investments?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "sold everything."},
                                {"value": "sold some."},
                                {"value": "did nothing."},
                                {"value": "reallocated my investments."},
                                {"value": "bought more."},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 8
            }
        }
    }, {"createItem": {
            "item": {
                "itemId": "286df58d",
                "title": "Question 5b",
                "pageBreakItem": {},
            },
            "location": {
                "index": 9
            }
        }
    }, {"createItem": {
            "item": {
                "title": "If you were ever to experience a 20% decline or more in the value of your investments in one year, what would you do?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "sell everything."},
                                {"value": "sell some."},
                                {"value": "do nothing."},
                                {"value": "reallocate my investments."},
                                {"value": "buy more."},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 10
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 6",
                "pageBreakItem": {},
            },
            "location": {
                "index": 11
            }
        }
    }, {"createItem": {
            "item": {
                "title": "When you hear “risk” related to your finances, what is the first thought that comes to mind?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "I try to avoid making decisions."},
                                {"value": "I reluctantly make decisions."},
                                {"value": "I confidently make decisions and don’t look back."},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 12
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 7",
                "pageBreakItem": {},
            },
            "location": {
                "index": 13
            }
        }
    }, {"createItem": {
            "item": {
                "title": "How much do you want to invest to get started?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "$5,000 to $25,000"},
                                {"value": "> $25,000"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 14
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 8",
                "pageBreakItem": {},
            },
            "location": {
                "index": 15
            }
        }
    }, {"createItem": {
            "item": {
                "title": "How much investment value fluctuation would you be comfortable with 1 year from now?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "−10% to 15%"},
                                {"value": "−15% to 25%"},
                                {"value": "−25% to 35%"},
                                {"value": "−30% to 45%"},
                                {"value": "−35% to 50%"},
                                {"value": "−40% to 55%"},
                                {"value": "−45% to 60%"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 16
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 9",
                "pageBreakItem": {},
            },
            "location": {
                "index": 17
            }
        }
    }, {"createItem": {
            "item": {
                "title": "How much investment value fluctuation would you be comfortable with 1 year from now?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "Monthly Contribution / Initial Investment < 10%"},
                                {"value": "Monthly Contribution / Initial Investment ≥ 10%"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 18
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 10a",
                "pageBreakItem": {},
            },
            "location": {
                "index": 19
            }
        }
    }, {"createItem": {
            "item": {
                "title": "How long do you need the income to last?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "1 to 4 years"},
                                {"value": "5 to 9 years"},
                                {"value": "10 to 19 years"},
                                {"value": "Over 19 years"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 20
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 10b",
                "pageBreakItem": {},
            },
            "location": {
                "index": 21
            }
        }
    }, {"createItem": {
            "item": {
                "title": "When will you need to start withdrawing funds from this account?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "1 year"},
                                {"value": "2 to 5 years"},
                                {"value": "6 to 10 years"},
                                {"value": "More than 10 years from now"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 22
            }
        }
    }, {"createItem": {
            "item": {
                "title": "Question 11",
                "pageBreakItem": {},
            },
            "location": {
                "index": 23
            }
        }
    }, {"createItem": {
            "item": {
                "title": "How would you consider yourself?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "Return strategy investor (i.e. prefer generating capital gains from stocks over fixed income from bonds)"},
                                {"value": "Income strategy investor (i.e. prefer generating fixed income like coupon or interest from bonds over capital gains from stocks)"},
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": 24
            }
        }
    }]
}

# Creates the initial form
result = form_service.forms().create(body=NEW_FORM).execute()

# Adds the question to the form
question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

# Prints the result to show the question has been added
get_result = form_service.forms().get(formId=result["formId"]).execute()
print(get_result)
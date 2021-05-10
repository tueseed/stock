def makeflexmessage():
    flex = {
                "type": "bubble",
                "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                          {
                                            "type": "text",
                                            "text": databack["symbol"],
                                            "weight": "bold",
                                            "size": "xl"
                                          },
                                          {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "spacing": "sm",
                                            "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                          {
                                                                            "type": "text",
                                                                            "text": "Place",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 1
                                                                          },
                                                                          {
                                                                            "type": "text",
                                                                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                                            "color": "#666666",
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                          }
                                                                        ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                          {
                                                                            "type": "text",
                                                                            "text": "Time",
                                                                            "color": "#aaaaaa",
                                                                            "size": "sm",
                                                                            "flex": 1
                                                                          },
                                                                          {
                                                                            "type": "text",
                                                                            "text": "10:00 - 23:00",
                                                                            "color": "#666666",
                                                                            "size": "sm",
                                                                            "flex": 5
                                                                          }
                                                                        ]
                                                        }
                                                        ]
                                        }
                                        ]
                                        }
                                        }
    return flex

def makecarousel(stockdata):
    carouselmsg = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": stockdata["symbol"],
                                            "size": "3xl",
                                            "align": "center"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "ราคาล่าสุด",
                                            "align": "end",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": stockdata["lastprice"],
                                            "align": "end",
                                            "size": "xl",
                                            "color": "#80ed99"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "เปลี่ยนแปลง"
                                        },
                                        {
                                            "type": "text",
                                            "text": stockdata["pricechange"],
                                            "color": "#80ed99"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "%เปลี่ยนแปลง",
                                            "align": "end"
                                        },
                                        {
                                            "type": "text",
                                            "text": stockdata["percentchange"],
                                            "align": "end",
                                            "color": "#80ed99"
                                        }
                                    ]
                                }
                            ]
                        },
                        {"type": "separator","margin": "lg"},
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                            {"type": "box","layout": "vertical",
                                                "contents": [{"type": "text","text": "ราคาปิดก่อนหน้า"}]
                                            },
                                            {"type": "box","layout": "vertical",
                                                "contents": [{"type": "text","text": stockdata["p_close"],"align": "end"}]
                                            }
                                        ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "lg",
                            "contents": [
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": "ราคาปิดก่อนหน้า"}]
                                 },
                                {"type": "box", "layout": "vertical",
                                 "contents": [{"type": "text", "text": stockdata["p_close"], "align": "end"}]
                                 }
                            ]
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "TRITN",
                                                    "size": "3xl",
                                                    "align": "center"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "ราคาล่าสุด",
                                                    "align": "end",
                                                    "size": "sm"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "999.99",
                                                    "align": "end",
                                                    "size": "xl",
                                                    "color": "#80ed99"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "เปลี่ยนแปลง"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "+0.99",
                                                    "color": "#80ed99"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "%เปลี่ยนแปลง",
                                                    "align": "end"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "+0.99",
                                                    "align": "end",
                                                    "color": "#80ed99"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
    return carouselmsg

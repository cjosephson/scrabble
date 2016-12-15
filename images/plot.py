import matplotlib.pyplot as plt
points = []

# vanilla AI, n=111
#scores = {0: (290, 535), 1: (461, 374), 2: (271, 388), 3: (253, 462), 4: (305, 302), 5: (243, 439), 6: (264, 420), 7: (247, 382), 8: (315, 488), 9: (322, 477), 10: (364, 309), 11: (293, 324), 12: (284, 309), 13: (301, 338), 14: (259, 335), 15: (308, 393), 16: (230, 278), 17: (280, 319), 18: (257, 362), 19: (325, 439), 20: (265, 485), 21: (246, 414), 22: (349, 363), 23: (220, 588), 24: (314, 317), 25: (206, 383), 26: (235, 356), 27: (269, 420), 28: (244, 350), 29: (250, 398), 30: (316, 408), 31: (310, 315), 32: (300, 425), 33: (368, 328), 34: (387, 479), 35: (322, 456), 36: (342, 502), 37: (348, 575), 38: (361, 391), 39: (283, 422), 40: (316, 433), 41: (205, 354), 42: (315, 513), 43: (308, 406), 44: (261, 439), 45: (261, 484), 46: (247, 454), 47: (284, 281), 48: (220, 561), 49: (258, 436), 50: (338, 538), 51: (270, 405), 52: (330, 243), 53: (278, 352), 54: (226, 447), 55: (277, 319), 56: (280, 331), 57: (355, 481), 58: (325, 272), 59: (254, 402), 60: (345, 470), 61: (265, 462), 62: (283, 298), 63: (294, 418), 64: (230, 375), 65: (278, 479), 66: (305, 476), 67: (280, 353), 68: (234, 291), 69: (296, 272), 70: (236, 457), 71: (273, 406), 72: (268, 583), 73: (235, 426), 74: (237, 366), 75: (324, 365), 76: (214, 251), 77: (390, 506), 78: (231, 484), 79: (206, 464), 80: (329, 547), 81: (176, 533), 82: (323, 349), 83: (302, 471), 84: (231, 394), 85: (233, 508), 86: (287, 425), 87: (234, 490), 88: (277, 389), 89: (266, 406), 90: (351, 349), 91: (319, 538), 92: (266, 590), 93: (327, 304), 94: (240, 248), 95: (252, 279), 96: (384, 378), 97: (304, 432), 98: (279, 445), 99: (249, 267)}

#rack heuristic only
#scores =  {0: (210, 575), 1: (297, 416), 2: (341, 397), 3: (281, 412), 4: (332, 556), 5: (233, 377), 6: (307, 383), 7: (185, 450), 8: (321, 515), 9: (231, 320), 10: (319, 379), 11: (321, 481), 12: (264, 400), 13: (242, 410), 14: (332, 397), 15: (269, 322), 16: (274, 451), 17: (342, 398), 18: (332, 415), 19: (243, 416), 20: (202, 568), 21: (250, 520), 22: (337, 366), 23: (329, 336), 24: (300, 495), 25: (254, 439), 26: (249, 486), 27: (233, 367), 28: (274, 376), 29: (350, 428), 30: (363, 478), 31: (297, 380), 32: (258, 289), 33: (483, 349), 34: (235, 319), 35: (341, 160), 36: (301, 343), 37: (384, 472), 38: (239, 364), 39: (240, 516), 40: (298, 231), 41: (256, 337), 42: (223, 287), 43: (309, 437), 44: (255, 368), 45: (326, 452), 46: (270, 414), 47: (288, 329), 48: (307, 456), 49: (265, 433), 50: (334, 277), 51: (253, 485), 52: (230, 372), 53: (337, 597), 54: (254, 323), 55: (243, 328), 56: (317, 295), 57: (290, 420), 58: (310, 347), 59: (326, 336), 60: (239, 371), 61: (298, 330), 62: (320, 416), 63: (320, 565), 64: (321, 545), 65: (241, 454), 66: (368, 457), 67: (389, 361), 68: (331, 349), 69: (333, 468), 70: (261, 206), 71: (272, 460), 72: (218, 476), 73: (251, 510), 74: (315, 440), 75: (219, 365), 76: (387, 382), 77: (254, 422), 78: (233, 352), 79: (266, 556), 80: (330, 698), 81: (290, 489), 82: (312, 401), 83: (296, 346), 84: (306, 441), 85: (286, 246), 86: (272, 255), 87: (268, 514), 88: (319, 525), 89: (284, 260), 90: (308, 477), 91: (304, 534), 92: (255, 252), 93: (231, 444), 94: (214, 611), 95: (248, 333), 96: (250, 505), 97: (309, 423), 98: (265, 493), 99: (338, 223)}

#partial mc
#scores = {0: (244, 258), 1: (257, 432), 2: (309, 287), 3: (285, 518), 4: (269, 285), 5: (231, 471), 6: (264, 513), 7: (321, 531), 8: (293, 469), 9: (228, 463), 10: (252, 531), 11: (243, 308), 12: (278, 312), 13: (259, 211), 14: (316, 301), 15: (225, 457), 16: (324, 227), 17: (334, 602), 18: (313, 253), 19: (238, 331), 20: (354, 478), 21: (286, 519), 22: (291, 451), 23: (281, 335), 24: (267, 342), 25: (370, 294), 26: (222, 367), 27: (348, 418), 28: (286, 445), 29: (295, 396), 30: (308, 233), 31: (313, 314), 32: (205, 607), 33: (179, 401), 34: (254, 269), 35: (300, 344), 36: (330, 416), 37: (270, 415), 38: (313, 352), 39: (213, 573), 40: (252, 375), 41: (338, 259), 42: (286, 288), 43: (312, 349), 44: (315, 446), 45: (314, 398), 46: (224, 365), 47: (306, 239), 48: (283, 558), 49: (254, 476), 50: (297, 492), 51: (347, 323), 52: (242, 479), 53: (351, 386), 54: (171, 343), 55: (276, 358), 56: (233, 315), 57: (337, 498), 58: (316, 416), 59: (285, 308), 60: (284, 485), 61: (277, 428), 62: (276, 341), 63: (274, 353), 64: (292, 372), 65: (321, 447), 66: (260, 470), 67: (258, 424), 68: (293, 387), 69: (345, 481), 70: (357, 449), 71: (274, 312), 72: (360, 322), 73: (316, 541), 74: (304, 428), 75: (258, 543), 76: (266, 374), 77: (354, 437), 78: (238, 377), 79: (293, 443), 80: (272, 416), 81: (254, 514), 82: (283, 387), 83: (254, 440), 84: (264, 500), 85: (308, 625), 86: (220, 338), 87: (363, 497), 88: (281, 299), 89: (213, 498), 90: (309, 244), 91: (283, 337), 92: (253, 410), 93: (255, 466), 94: (214, 475), 95: (325, 375), 96: (333, 413), 97: (321, 457), 98: (168, 437), 99: (350, 253)}

# vanilla self vs self (half A first, half B first)
#scores = {0: (449, 348), 1: (424, 343), 2: (385, 264), 3: (412, 369), 4: (373, 477), 5: (378, 308), 6: (412, 426), 7: (444, 310), 8: (318, 352), 9: (392, 364), 10: (388, 385), 11: (429, 356), 12: (341, 447), 13: (296, 478), 14: (397, 377), 15: (355, 303), 16: (363, 263), 17: (328, 396), 18: (353, 337), 19: (433, 369), 20: (469, 375), 21: (436, 374), 22: (423, 317), 23: (409, 282), 24: (458, 367), 25: (390, 355), 26: (461, 351), 27: (365, 454), 28: (501, 332), 29: (359, 407), 30: (337, 317), 31: (303, 326), 32: (442, 445), 33: (399, 278), 34: (361, 323), 35: (259, 317), 36: (338, 296), 37: (479, 333), 38: (349, 296), 39: (320, 222), 40: (371, 306), 41: (374, 311), 42: (333, 311), 43: (274, 306), 44: (460, 395), 45: (426, 407), 46: (410, 338), 47: (347, 332), 48: (371, 397), 49: (321, 284), 50: (351, 295), 51: (278, 419), 52: (341, 356), 53: (373, 460), 54: (319, 362), 55: (368, 374), 56: (317, 447), 57: (363, 366), 58: (331, 348), 59: (264, 377), 60: (276, 260), 61: (355, 370), 62: (385, 382), 63: (364, 385), 64: (328, 427), 65: (455, 327), 66: (368, 326), 67: (410, 323), 68: (338, 325), 69: (374, 484), 70: (409, 372), 71: (370, 347), 72: (408, 381), 73: (306, 400), 74: (301, 340), 75: (416, 385), 76: (258, 352), 77: (377, 377), 78: (328, 349), 79: (286, 309), 80: (329, 321), 81: (331, 325), 82: (304, 431), 83: (386, 475), 84: (298, 303), 85: (340, 336), 86: (361, 406), 87: (377, 443), 88: (318, 265), 89: (427, 284), 90: (355, 373), 91: (290, 380), 92: (288, 384), 93: (416, 380), 94: (374, 362), 95: (337, 384), 96: (356, 361), 97: (388, 378), 98: (335, 398), 99: (362, 380)}

# vanilla self vs self (all A first)
#scores = {0: (449, 348), 1: (424, 343), 2: (385, 264), 3: (412, 369), 4: (373, 477), 5: (378, 308), 6: (412, 426), 7: (444, 310), 8: (318, 352), 9: (392, 364), 10: (388, 385), 11: (429, 356), 12: (341, 447), 13: (296, 478), 14: (397, 377), 15: (355, 303), 16: (363, 263), 17: (328, 396), 18: (353, 337), 19: (433, 369), 20: (469, 375), 21: (436, 374), 22: (423, 317), 23: (409, 282), 24: (458, 367), 25: (390, 355), 26: (461, 351), 27: (365, 454), 28: (501, 332), 29: (359, 407), 30: (337, 317), 31: (303, 326), 32: (442, 445), 33: (399, 278), 34: (361, 323), 35: (259, 317), 36: (338, 296), 37: (479, 333), 38: (349, 296), 39: (320, 222), 40: (371, 306), 41: (374, 311), 42: (333, 311), 43: (274, 306), 44: (460, 395), 45: (426, 407), 46: (410, 338), 47: (347, 332), 48: (371, 397), 49: (321, 284), 50: (351, 295), 51: (319, 306), 52: (342, 270), 53: (527, 285), 54: (306, 350), 55: (392, 313), 56: (348, 292), 57: (316, 349), 58: (318, 321), 59: (442, 322), 60: (351, 336), 61: (319, 373), 62: (379, 392), 63: (335, 377), 64: (466, 384), 65: (330, 389), 66: (355, 447), 67: (349, 296), 68: (348, 321), 69: (354, 331), 70: (353, 419), 71: (355, 286), 72: (363, 384), 73: (360, 236), 74: (433, 326), 75: (365, 297), 76: (342, 279), 77: (351, 299), 78: (302, 375), 79: (447, 385), 80: (454, 436), 81: (278, 367), 82: (339, 412), 83: (346, 416), 84: (305, 409), 85: (336, 367), 86: (335, 287), 87: (353, 318), 88: (240, 282), 89: (401, 333), 90: (334, 354), 91: (404, 395), 92: (397, 407), 93: (334, 438), 94: (347, 382), 95: (343, 367), 96: (341, 469), 97: (399, 353), 98: (345, 300), 99: (374, 328)}


# vanilla self vs self (all B first)
#scores =  {0: (121, 118), 1: (387, 435), 2: (602, 448), 3: (294, 314), 4: (354, 383), 5: (308, 296), 6: (314, 382), 7: (336, 311), 8: (305, 342), 9: (362, 318), 10: (280, 350), 11: (321, 407), 12: (338, 341), 13: (409, 393), 14: (397, 412), 15: (281, 271), 16: (405, 333), 17: (291, 354), 18: (320, 388), 19: (344, 396), 20: (326, 263), 21: (306, 401), 22: (334, 393), 23: (286, 367), 24: (384, 348), 25: (299, 318), 26: (314, 341), 27: (387, 280), 28: (470, 320), 29: (325, 366), 30: (313, 355), 31: (317, 470), 32: (367, 365), 33: (311, 250), 34: (301, 349), 35: (268, 402), 36: (354, 436), 37: (324, 317), 38: (531, 360), 39: (528, 374), 40: (324, 363), 41: (356, 388), 42: (314, 367), 43: (403, 463), 44: (325, 365), 45: (292, 329), 46: (335, 291), 47: (407, 398), 48: (432, 332), 49: (287, 348), 50: (287, 443), 51: (278, 419), 52: (341, 356), 53: (373, 460), 54: (319, 362), 55: (368, 374), 56: (317, 447), 57: (363, 366), 58: (331, 348), 59: (264, 377), 60: (276, 260), 61: (355, 370), 62: (385, 382), 63: (364, 385), 64: (328, 427), 65: (455, 327), 66: (368, 326), 67: (410, 323), 68: (338, 325), 69: (374, 484), 70: (409, 372), 71: (370, 347), 72: (408, 381), 73: (306, 400), 74: (301, 340), 75: (416, 385), 76: (258, 352), 77: (377, 377), 78: (328, 349), 79: (286, 309), 80: (329, 321), 81: (331, 325), 82: (304, 431), 83: (386, 475), 84: (298, 303), 85: (340, 336), 86: (361, 406), 87: (377, 443), 88: (318, 265), 89: (427, 284), 90: (355, 373), 91: (290, 380), 92: (288, 384), 93: (416, 380), 94: (374, 362), 95: (337, 384), 96: (356, 361), 97: (388, 378), 98: (335, 398), 99: (362, 380)}


# vanilla self vs self (all B first, run 2)
#scores = {0: (313, 463), 1: (341, 328), 2: (464, 317), 3: (375, 370), 4: (300, 367), 5: (315, 335), 6: (321, 332), 7: (342, 454), 8: (247, 436), 9: (370, 312), 10: (309, 340), 11: (384, 302), 12: (312, 336), 13: (310, 335), 14: (420, 328), 15: (355, 455), 16: (272, 471), 17: (319, 382), 18: (375, 321), 19: (331, 399), 20: (441, 354), 21: (348, 304), 22: (377, 279), 23: (381, 422), 24: (361, 347), 25: (389, 382), 26: (345, 349), 27: (324, 351), 28: (293, 429), 29: (328, 358), 30: (310, 244), 31: (402, 362), 32: (375, 380), 33: (418, 346), 34: (354, 348), 35: (371, 329), 36: (373, 394), 37: (358, 338), 38: (408, 391), 39: (340, 359), 40: (387, 325), 41: (287, 321), 42: (336, 452), 43: (306, 327), 44: (305, 361), 45: (290, 332), 46: (355, 426), 47: (315, 306), 48: (445, 323), 49: (293, 450), 50: (383, 341), 51: (370, 345), 52: (348, 393), 53: (371, 328), 54: (310, 406), 55: (371, 341), 56: (288, 378), 57: (365, 351), 58: (310, 438), 59: (338, 311), 60: (405, 360), 61: (288, 472), 62: (255, 329), 63: (372, 327), 64: (343, 385), 65: (356, 390), 66: (377, 322), 67: (327, 369), 68: (317, 373), 69: (298, 345), 70: (271, 406), 71: (338, 374), 72: (340, 418), 73: (391, 401), 74: (322, 286), 75: (276, 344), 76: (323, 419), 77: (321, 382), 78: (283, 363), 79: (327, 326), 80: (359, 451), 81: (409, 399), 82: (369, 339), 83: (405, 443), 84: (340, 347), 85: (345, 388), 86: (393, 298), 87: (367, 408), 88: (305, 398), 89: (319, 352), 90: (300, 390), 91: (456, 401), 92: (338, 357), 93: (380, 299), 94: (353, 311), 95: (398, 400), 96: (340, 358), 97: (244, 442), 98: (337, 350), 99: (391, 417)}


#rackH self vs self (half A first, half B first)
#scores = {0: (376, 458), 1: (296, 314), 2: (313, 328), 3: (371, 327), 4: (466, 361), 5: (402, 355), 6: (345, 345), 7: (342, 388), 8: (425, 264), 9: (379, 350), 10: (357, 298), 11: (380, 410), 12: (354, 290), 13: (475, 414), 14: (395, 344), 15: (371, 260), 16: (336, 325), 17: (368, 291), 18: (334, 294), 19: (431, 308), 20: (305, 348), 21: (316, 348), 22: (458, 332), 23: (367, 304), 24: (267, 306), 25: (437, 280), 26: (284, 381), 27: (353, 342), 28: (448, 414), 29: (268, 353), 30: (341, 312), 31: (486, 344), 32: (282, 325), 33: (384, 338), 34: (281, 334), 35: (458, 394), 36: (423, 347), 37: (356, 321), 38: (345, 343), 39: (330, 392), 40: (362, 280), 41: (368, 300), 42: (327, 292), 43: (390, 418), 44: (385, 342), 45: (392, 390), 46: (313, 335), 47: (481, 407), 48: (314, 359), 49: (355, 373), 50: (317, 390), 51: (344, 310), 52: (327, 288), 53: (346, 373), 54: (332, 332), 55: (379, 344), 56: (391, 346), 57: (398, 367), 58: (451, 355), 59: (384, 366), 60: (443, 342), 61: (324, 375), 62: (360, 351), 63: (417, 335), 64: (384, 347), 65: (330, 288), 66: (285, 358), 67: (405, 334), 68: (356, 317), 69: (419, 430), 70: (397, 375), 71: (337, 377), 72: (396, 373), 73: (285, 337), 74: (333, 368), 75: (344, 316), 76: (297, 343), 77: (365, 408), 78: (416, 338), 79: (381, 369), 80: (317, 285), 81: (302, 349), 82: (357, 326), 83: (385, 262), 84: (329, 368), 85: (453, 293), 86: (299, 322), 87: (462, 349), 88: (496, 354), 89: (324, 340), 90: (328, 302), 91: (399, 427), 92: (343, 333), 93: (363, 301), 94: (365, 274), 95: (299, 294), 96: (380, 301), 97: (305, 310), 98: (376, 282), 99: (452, 321)}

# rackH self vs self (all A first, run 2)
#scores = {0: (383, 481), 1: (396, 386), 2: (345, 427), 3: (338, 243), 4: (279, 361), 5: (322, 369), 6: (350, 290), 7: (321, 372), 8: (465, 387), 9: (345, 314), 10: (324, 366), 11: (310, 265), 12: (335, 413), 13: (348, 321), 14: (325, 346), 15: (372, 365), 16: (331, 358), 17: (430, 374), 18: (308, 377), 19: (307, 308), 20: (351, 426), 21: (390, 384), 22: (335, 369), 23: (319, 399), 24: (369, 404), 25: (398, 344), 26: (353, 353), 27: (494, 293), 28: (359, 390), 29: (371, 421), 30: (326, 438), 31: (387, 400), 32: (410, 343), 33: (301, 313), 34: (354, 382), 35: (287, 323), 36: (347, 338), 37: (387, 361), 38: (331, 363), 39: (320, 471), 40: (310, 323), 41: (318, 380), 42: (392, 274), 43: (407, 351), 44: (417, 314), 45: (368, 446), 46: (298, 292), 47: (370, 417), 48: (315, 289), 49: (353, 400), 50: (310, 364), 51: (380, 368), 52: (258, 380), 53: (397, 338), 54: (407, 337), 55: (344, 310), 56: (359, 367), 57: (375, 342), 58: (363, 434), 59: (387, 414), 60: (406, 355), 61: (408, 363), 62: (317, 313), 63: (377, 417), 64: (337, 275), 65: (256, 193), 66: (424, 364), 67: (355, 374), 68: (379, 313), 69: (423, 347), 70: (327, 385), 71: (332, 353), 72: (351, 362), 73: (370, 363), 74: (300, 355), 75: (312, 381), 76: (383, 394), 77: (311, 294), 78: (363, 369), 79: (363, 373), 80: (367, 400), 81: (390, 373), 82: (352, 419), 83: (321, 397), 84: (360, 309), 85: (255, 508), 86: (369, 399), 87: (330, 368), 88: (390, 349), 89: (354, 336), 90: (448, 354), 91: (428, 396), 92: (335, 365), 93: (316, 449), 94: (329, 247), 95: (337, 381), 96: (354, 411), 97: (311, 314), 98: (371, 378), 99: (346, 363)}

# rackH self vs self (all A first)
#scores = {0: (376, 458), 1: (296, 314), 2: (313, 328), 3: (371, 327), 4: (466, 361), 5: (402, 355), 6: (345, 345), 7: (342, 388), 8: (425, 264), 9: (379, 350), 10: (357, 298), 11: (380, 410), 12: (354, 290), 13: (475, 414), 14: (395, 344), 15: (371, 260), 16: (336, 325), 17: (368, 291), 18: (334, 294), 19: (431, 308), 20: (305, 348), 21: (316, 348), 22: (458, 332), 23: (367, 304), 24: (267, 306), 25: (437, 280), 26: (284, 381), 27: (353, 342), 28: (448, 414), 29: (268, 353), 30: (341, 312), 31: (486, 344), 32: (282, 325), 33: (384, 338), 34: (281, 334), 35: (458, 394), 36: (423, 347), 37: (356, 321), 38: (345, 343), 39: (330, 392), 40: (362, 280), 41: (368, 300), 42: (327, 292), 43: (390, 418), 44: (385, 342), 45: (392, 390), 46: (313, 335), 47: (481, 407), 48: (314, 359), 49: (355, 373), 50: (317, 390), 51: (366, 290), 52: (290, 322), 53: (239, 413), 54: (355, 381), 55: (403, 337), 56: (368, 313), 57: (282, 452), 58: (308, 369), 59: (305, 334), 60: (337, 368), 61: (277, 336), 62: (317, 294), 63: (409, 377), 64: (342, 411), 65: (359, 361), 66: (367, 305), 67: (398, 369), 68: (356, 381), 69: (300, 357), 70: (331, 406), 71: (326, 351), 72: (358, 288), 73: (391, 343), 74: (224, 254), 75: (270, 351), 76: (298, 343), 77: (353, 413), 78: (322, 366), 79: (368, 345), 80: (315, 378), 81: (366, 311), 82: (317, 424), 83: (289, 292), 84: (320, 351), 85: (282, 373), 86: (323, 300), 87: (344, 359), 88: (349, 330), 89: (356, 410), 90: (285, 390), 91: (317, 315), 92: (364, 403), 93: (332, 389), 94: (333, 359), 95: (295, 388), 96: (251, 391), 97: (465, 395), 98: (310, 412), 99: (391, 345)}

# rackH self vs self (all B first)
#scores = {0: (356, 351), 1: (334, 287), 2: (341, 319), 3: (333, 482), 4: (402, 339), 5: (351, 432), 6: (374, 358), 7: (365, 297), 8: (351, 398), 9: (361, 396), 10: (358, 356), 11: (320, 466), 12: (300, 386), 13: (327, 360), 14: (427, 306), 15: (309, 422), 16: (312, 362), 17: (304, 310), 18: (390, 333), 19: (260, 424), 20: (347, 397), 21: (368, 403), 22: (360, 314), 23: (306, 351), 24: (303, 376), 25: (323, 314), 26: (393, 370), 27: (314, 369), 28: (408, 396), 29: (331, 342), 30: (349, 294), 31: (317, 351), 32: (356, 416), 33: (377, 339), 34: (319, 331), 35: (291, 370), 36: (304, 442), 37: (215, 264), 38: (276, 349), 39: (351, 346), 40: (329, 395), 41: (284, 330), 42: (310, 423), 43: (414, 474), 44: (250, 286), 45: (412, 322), 46: (378, 355), 47: (331, 339), 48: (267, 228), 49: (398, 354), 50: (321, 314), 51: (344, 310), 52: (327, 288), 53: (346, 373), 54: (332, 332), 55: (379, 344), 56: (391, 346), 57: (398, 367), 58: (451, 355), 59: (384, 366), 60: (443, 342), 61: (324, 375), 62: (360, 351), 63: (417, 335), 64: (384, 347), 65: (330, 288), 66: (285, 358), 67: (405, 334), 68: (356, 317), 69: (419, 430), 70: (397, 375), 71: (337, 377), 72: (396, 373), 73: (285, 337), 74: (333, 368), 75: (344, 316), 76: (297, 343), 77: (365, 408), 78: (416, 338), 79: (381, 369), 80: (317, 285), 81: (302, 349), 82: (357, 326), 83: (385, 262), 84: (329, 368), 85: (453, 293), 86: (299, 322), 87: (462, 349), 88: (496, 354), 89: (324, 340), 90: (328, 302), 91: (399, 427), 92: (343, 333), 93: (363, 301), 94: (365, 274), 95: (299, 294), 96: (380, 301), 97: (305, 310), 98: (376, 282), 99: (452, 321)}

#partial mc vs vanilla
scores = {0: (334, 293), 1: (288, 410), 2: (363, 396), 3: (304, 366), 4: (332, 308), 5: (336, 345), 6: (302, 318), 7: (280, 346), 8: (335, 378), 9: (305, 372), 10: (306, 370), 11: (329, 426), 12: (298, 426), 13: (336, 336), 14: (339, 426), 15: (372, 369), 16: (251, 345), 17: (281, 316), 18: (327, 337), 19: (318, 385), 20: (292, 331), 21: (407, 292), 22: (335, 462), 23: (301, 357), 24: (415, 396)}

for p in scores.itervalues(): points.append(p)

scores = {0: (376, 386), 1: (324, 313), 2: (356, 365), 3: (312, 303), 4: (389, 376), 5: (370, 385), 6: (246, 391), 7: (280, 322), 8: (433, 344), 9: (300, 332), 10: (337, 311), 11: (265, 366), 12: (408, 392), 13: (454, 330), 14: (296, 346), 15: (306, 306), 16: (306, 407), 17: (321, 325), 18: (368, 375), 19: (413, 384), 20: (367, 342), 21: (341, 343), 22: (337, 382), 23: (461, 375), 24: (315, 389), 25: (384, 453), 26: (344, 420), 27: (352, 344), 28: (269, 355), 29: (330, 337), 30: (284, 356), 31: (326, 459), 32: (335, 324), 33: (383, 337), 34: (337, 413), 35: (323, 367), 36: (326, 347), 37: (451, 423), 38: (401, 321), 39: (342, 334), 40: (355, 357), 41: (237, 407)}

for p in scores.itervalues(): points.append(p)

print "points",points
deltas = []
ratios = []
heur = 0
van = 0
quack = 0
cs221 = 0
numGames = len(points)
#######################################
for p in points:
    heur += p[0]
    van += p[1]
    ratios.append(p[0]/float(p[1]))
    deltas.append(p[0] - p[1])
deltas = sorted(deltas)
ratios = sorted(ratios)
winRate = 0
smashedRate = 0
smashingRate = 0
for g in ratios:
    if g >= 2:
        smashingRate += 1
    if g > 1:
        winRate += 1
    if g <= 0.5:
        smashedRate +=1
winRate = winRate/float(numGames)
smashedRate = smashedRate/float(numGames)
smashingRate = smashingRate/float(numGames)
print "deltas",deltas
print "num games", numGames
print "A avg",heur/float(numGames)
print "B avg",van/float(numGames)
print "avg delta",sum(deltas)/float(numGames)
print "A win rate",winRate
print "A smashed rate",smashedRate
print "A smashing rate",smashingRate
print "best ratio", 1.0/ratios[0]
print "ratios",ratios
#########################################
# for p in points:
#     quack += p[0]
#     cs221 += p[1]
#     ratios.append(p[1]/float(p[0]))
#     deltas.append(p[1] - p[0])
# deltas = sorted(deltas)
# ratios = sorted(ratios)
# winRate = 0
# smashedRate = 0
# smashingRate = 0
# for g in ratios:
#     if g <= 0.5:
#         smashingRate += 1
#     if g < 1:
#         winRate += 1
#     if g >=2:
#         smashedRate +=1
# winRate = winRate/float(numGames)
# smashedRate = smashedRate/float(numGames)
# smashingRate = smashingRate/float(numGames)
# print "deltas",deltas
# print "num games", numGames
# print "quack avg",quack/float(numGames)
# print "cs221 avg",cs221/float(numGames)
# print "avg delta",sum(deltas)/float(numGames)
# print "cs221 win rate",winRate
# print "cs221 smashed rate",smashedRate
# print "cs221 smashing rate",smashingRate
# print "best ratio", 1.0/ratios[0]
# print "ratios",ratios
##########################################
plt.bar(range(numGames), deltas, color="yellow")
#plt.plot([i for i in xrange(len(us))], us, label="cs221", marker = '.')
#plt.plot([i for i in xrange(len(quackle))], quackle, label="quackle", marker = '.')
#plt.title('cs221 Selfplay Score Differentials')
plt.title('Quackle vs Monte Carlo')
plt.xlabel("game number")
#plt.ylim([0, 600])
plt.ylabel("Quackle Score - cs221 Score")
plt.legend()
plt.show()

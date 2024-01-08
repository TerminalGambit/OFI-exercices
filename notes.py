grades = """
22307026 ABI
22204374 ABI
22207028 9,5 10,5
21804381 2 2,5
22004684 ABI
20504084 3 3,5
22102678 7 8
22310956 5,5 6,5
22208976 6 7
22208784 1 1,5
22212224 9,5 10,5
21914552 ABI
22201300 2 2,5
22210754 6 7
22116899 ABI
21913981 ABI
22011818 ABI
22207203 6 7
22015893 1 1,5
22212243 4,5 5
22209783 6 7
22201416 11,5 13
22105905 10 11
22307479 1 1,5
22201026 3 3,5
22200336 11 12,5
21907278 1 1,5
21900638 1 1,5
22203503 4 4,5
22209340 4 4,5
22100448 1 1,5
22200641 7 8
22200969 2 2,5
22206302 13 14,5
22003331 ABI
22201857 2 2,5
22205090 1 1,5
22204830 4 4,5
22116789 4,5 5
21602528 ABI
22306981 5,5 6,5
22101334 1 1,5
22016573 1 1,5
22201315 1 1,5
21704226 8,5 9,5
22005707 ABI
22309458 8,5 9,5
22202611 ABI
22208435 2 2,5
22206759 4 4,5
22109694 17 19
22205857 ABI
22208486 1 1,5
22101956 ABI
22116709 12 13,5
22113167 ABI
22015401 1 1,5
22209690 1 1,5
22109373 2 2,5
22205244 4 4,5
22203502 9 10
22110398 1 1,5
22106326 1 1,5
22200301 10 11
22116785 13 14,5
22008483 1 1,5
22207347 3 3,5
22211271 4 4,5
22208105 3 3,5
22204806 1 1,5
22205017 2 2,5
22212818 4 4,5
22102243 1 1,5
22204089 8 9
22103522 ABI
22104419 ABI
22200807 7 8
22304823 2 2,5
22210627 ABI
22207551 8 9
22207560 ABI
22306400 6 7
22212704 1 1,5
22311632 2 2,5
22103559 1 1,5
22204144 6 7
22210302 3 3,5
22021011 ABI
22211628 ABI
22311101 11 12,5
22208272 11 12,5
22103535 2 2,5
22007523 ABI
22102365 4 4,5
22210703 1 1,5
22012565 5 5,5
22201239 1,5 2
22206278 1 1,5
22203612 6 7
21702656 ABI
22101125 8 9
21808599 14 15,5
22206581 3,5 4
22107569 4 4,5
22112232 ABI
22102516 4 4,5
22112346 1,5 2
22000383 4 4,5
22210880 9 10
22101301 5 5,5
22117083 20 20
22216029 ABI
21812006 3 3,5
22105210 2 2,5
22206309 8 9
22101685 10 11
22103231 6,5 7,5
22207333 8 9
22209969 9 10
22211287 5 5,5
22200325 2 2,5
22002169 ABI
21908724 ABI
22205022 3,5 4
22202681 1 1,5
21812377 2 2,5
"""

grades = grades.split("\n")
grades = [grade.split(" ") for grade in grades]

grades = [(grade[0], grade[1], grade[2]) for grade in grades if len(grade) == 3]
grades = [(grade[0], grade[1], grade[2]) for grade in grades if grade[2] != "ABI"]

average = sum([float(grade[2].replace(",", ".")) for grade in grades]) / len(grades)
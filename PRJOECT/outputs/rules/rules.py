def findDecision(obj): #obj[0]: age, obj[1]: workclass, obj[2]: educational-num, obj[3]: marital-status, obj[4]: occupation, obj[5]: relationship, obj[6]: race, obj[7]: gender, obj[8]: capital-gain, obj[9]: capital-loss, obj[10]: hours-per-week, obj[11]: native-country
	# {"feature": "marital-status", "instances": 48842, "metric_value": 0.0504, "depth": 1}
	if obj[3]<=2:
		# {"feature": "educational-num", "instances": 29049, "metric_value": 0.0319, "depth": 2}
		if obj[2]<=12:
			# {"feature": "capital-gain", "instances": 21039, "metric_value": 0.0227, "depth": 3}
			if obj[8]<=6082.379545993911:
				# {"feature": "relationship", "instances": 20291, "metric_value": 0.0166, "depth": 4}
				if obj[5]<=0:
					# {"feature": "hours-per-week", "instances": 13227, "metric_value": 0.0059, "depth": 5}
					if obj[10]>31.75711455488132:
						# {"feature": "age", "instances": 12242, "metric_value": 0.0069, "depth": 6}
						if obj[0]>30.959874792851664:
							# {"feature": "capital-loss", "instances": 10328, "metric_value": 0.0035, "depth": 7}
							if obj[9]<=1415.384598641499:
								# {"feature": "workclass", "instances": 9744, "metric_value": 0.0033, "depth": 8}
								if obj[1]<=5:
									# {"feature": "native-country", "instances": 8941, "metric_value": 0.002, "depth": 9}
									if obj[11]>36.52589195839391:
										# {"feature": "occupation", "instances": 8219, "metric_value": 0.0012, "depth": 10}
										if obj[4]>3:
											# {"feature": "race", "instances": 4808, "metric_value": 0.0006, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 4758, "metric_value": 0.0001, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.0
											elif obj[6]<=0:
												# {"feature": "gender", "instances": 50, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.12
											else: return 0.12
										elif obj[4]<=3:
											# {"feature": "race", "instances": 3411, "metric_value": 0.0004, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 3346, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.37089061566049014
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 65, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.24615384615384617
											else: return 0.24615384615384617
										else: return 0.3685136323658751
									elif obj[11]<=36.52589195839391:
										# {"feature": "occupation", "instances": 722, "metric_value": 0.0106, "depth": 10}
										if obj[4]<=7:
											# {"feature": "race", "instances": 562, "metric_value": 0.0015, "depth": 11}
											if obj[6]>2:
												# {"feature": "gender", "instances": 465, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.13978494623655913
											elif obj[6]<=2:
												# {"feature": "gender", "instances": 97, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.20618556701030927
											else: return 0.20618556701030927
										elif obj[4]>7:
											# {"feature": "race", "instances": 160, "metric_value": 0.0022, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 159, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.33962264150943394
											elif obj[6]<=0:
												return 0
											else: return 0.0
										else: return 0.3375
									else: return 0.1925207756232687
								elif obj[1]>5:
									# {"feature": "occupation", "instances": 803, "metric_value": 0.0045, "depth": 9}
									if obj[4]<=3:
										# {"feature": "native-country", "instances": 483, "metric_value": 0.0018, "depth": 10}
										if obj[11]>1:
											# {"feature": "race", "instances": 481, "metric_value": 0.0007, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 467, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5674518201284796
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 14, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.7142857142857143
											else: return 0.7142857142857143
										elif obj[11]<=1:
											return 1
										else: return 1.0
									elif obj[4]>3:
										# {"feature": "native-country", "instances": 320, "metric_value": 0.0055, "depth": 10}
										if obj[11]>4:
											# {"feature": "race", "instances": 316, "metric_value": 0.0043, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 313, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.4472843450479233
											elif obj[6]<=0:
												return 0
											else: return 0.0
										elif obj[11]<=4:
											return 0
										else: return 0.0
									else: return 0.4375
								else: return 0.5193026151930261
							elif obj[9]>1415.384598641499:
								# {"feature": "occupation", "instances": 584, "metric_value": 0.0033, "depth": 8}
								if obj[4]<=7:
									# {"feature": "native-country", "instances": 376, "metric_value": 0.0034, "depth": 9}
									if obj[11]>30:
										# {"feature": "workclass", "instances": 356, "metric_value": 0.0024, "depth": 10}
										if obj[1]<=5:
											# {"feature": "race", "instances": 317, "metric_value": 0.0015, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 316, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5379746835443038
											elif obj[6]<=0:
												return 1
											else: return 1.0
										elif obj[1]>5:
											# {"feature": "race", "instances": 39, "metric_value": 0.0086, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 38, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6842105263157895
											elif obj[6]<=1:
												return 1
											else: return 1.0
										else: return 0.6923076923076923
									elif obj[11]<=30:
										# {"feature": "workclass", "instances": 20, "metric_value": 0.0358, "depth": 10}
										if obj[1]<=2:
											# {"feature": "race", "instances": 15, "metric_value": 0.0349, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.23076923076923078
											elif obj[6]<=1:
												return 0
											else: return 0.0
										elif obj[1]>2:
											# {"feature": "race", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[6]<=4:
												# {"feature": "gender", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6
											else: return 0.6
										else: return 0.6
									else: return 0.3
								elif obj[4]>7:
									# {"feature": "workclass", "instances": 208, "metric_value": 0.0037, "depth": 9}
									if obj[1]<=3:
										# {"feature": "native-country", "instances": 162, "metric_value": 0.0019, "depth": 10}
										if obj[11]>30:
											# {"feature": "race", "instances": 155, "metric_value": 0.001, "depth": 11}
											if obj[6]>2:
												# {"feature": "gender", "instances": 142, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.647887323943662
											elif obj[6]<=2:
												# {"feature": "gender", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5384615384615384
											else: return 0.5384615384615384
										elif obj[11]<=30:
											# {"feature": "race", "instances": 7, "metric_value": 0.0021, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.4
											elif obj[6]<=1:
												return 0.5
											else: return 0.5
										else: return 0.42857142857142855
									elif obj[1]>3:
										# {"feature": "race", "instances": 46, "metric_value": 0.0187, "depth": 10}
										if obj[6]>2:
											# {"feature": "native-country", "instances": 43, "metric_value": 0.0139, "depth": 11}
											if obj[11]>4:
												# {"feature": "gender", "instances": 41, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.7317073170731707
											elif obj[11]<=4:
												return 1
											else: return 1.0
										elif obj[6]<=2:
											return 1
										else: return 1.0
									else: return 0.7608695652173914
								else: return 0.6586538461538461
							else: return 0.583904109589041
						elif obj[0]<=30.959874792851664:
							# {"feature": "workclass", "instances": 1914, "metric_value": 0.0048, "depth": 7}
							if obj[1]<=3:
								# {"feature": "capital-loss", "instances": 1722, "metric_value": 0.007, "depth": 8}
								if obj[9]<=1740:
									# {"feature": "occupation", "instances": 1678, "metric_value": 0.0018, "depth": 9}
									if obj[4]<=7:
										# {"feature": "native-country", "instances": 1217, "metric_value": 0.0008, "depth": 10}
										if obj[11]>25.3053395105307:
											# {"feature": "race", "instances": 1110, "metric_value": 0.0003, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 1083, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.12096029547553093
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 27, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.18518518518518517
											else: return 0.18518518518518517
										elif obj[11]<=25.3053395105307:
											# {"feature": "race", "instances": 107, "metric_value": 0.0067, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 102, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.0784313725490196
											elif obj[6]<=1:
												return 0
											else: return 0.0
										else: return 0.07476635514018691
									elif obj[4]>7:
										# {"feature": "race", "instances": 461, "metric_value": 0.0032, "depth": 10}
										if obj[6]>3:
											# {"feature": "native-country", "instances": 419, "metric_value": 0.0115, "depth": 11}
											if obj[11]>28:
												# {"feature": "gender", "instances": 399, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.19298245614035087
											elif obj[11]<=28:
												return 0
											else: return 0.0
										elif obj[6]<=3:
											# {"feature": "native-country", "instances": 42, "metric_value": 0.0651, "depth": 11}
											if obj[11]>29:
												# {"feature": "gender", "instances": 38, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.02631578947368421
											elif obj[11]<=29:
												return 0.5
											else: return 0.5
										else: return 0.07142857142857142
									else: return 0.1735357917570499
								elif obj[9]>1740:
									# {"feature": "race", "instances": 44, "metric_value": 0.0322, "depth": 9}
									if obj[6]>2:
										# {"feature": "occupation", "instances": 41, "metric_value": 0.0257, "depth": 10}
										if obj[4]>0:
											# {"feature": "native-country", "instances": 39, "metric_value": 0.0001, "depth": 11}
											if obj[11]>32:
												# {"feature": "gender", "instances": 37, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5405405405405406
											elif obj[11]<=32:
												return 0.5
											else: return 0.5
										elif obj[4]<=0:
											return 0
										else: return 0.0
									elif obj[6]<=2:
										return 1
									else: return 1.0
								else: return 0.5454545454545454
							elif obj[1]>3:
								# {"feature": "occupation", "instances": 192, "metric_value": 0.0049, "depth": 8}
								if obj[4]<=9:
									# {"feature": "native-country", "instances": 104, "metric_value": 0.0091, "depth": 9}
									if obj[11]>37:
										# {"feature": "race", "instances": 97, "metric_value": 0.0113, "depth": 10}
										if obj[6]>1:
											# {"feature": "capital-loss", "instances": 93, "metric_value": 0.003, "depth": 11}
											if obj[9]<=1887:
												# {"feature": "gender", "instances": 92, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.2391304347826087
											elif obj[9]>1887:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 0
										else: return 0.0
									elif obj[11]<=37:
										# {"feature": "race", "instances": 7, "metric_value": 0.1449, "depth": 10}
										if obj[6]>2:
											# {"feature": "gender", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.4
											else: return 0.4
										elif obj[6]<=2:
											return 1
										else: return 1.0
									else: return 0.5714285714285714
								elif obj[4]>9:
									# {"feature": "native-country", "instances": 88, "metric_value": 0.0134, "depth": 9}
									if obj[11]>10:
										# {"feature": "race", "instances": 85, "metric_value": 0.0227, "depth": 10}
										if obj[6]>1:
											# {"feature": "capital-loss", "instances": 82, "metric_value": 0.0047, "depth": 11}
											if obj[9]<=1977:
												# {"feature": "gender", "instances": 81, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.37037037037037035
											elif obj[9]>1977:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 1
										else: return 1.0
									elif obj[11]<=10:
										return 0
									else: return 0.0
								else: return 0.375
							else: return 0.3072916666666667
						else: return 0.16039707419017765
					elif obj[10]<=31.75711455488132:
						# {"feature": "capital-loss", "instances": 985, "metric_value": 0.0056, "depth": 6}
						if obj[9]<=742.0390775674279:
							# {"feature": "age", "instances": 954, "metric_value": 0.0063, "depth": 7}
							if obj[0]>23.049242554348005:
								# {"feature": "occupation", "instances": 916, "metric_value": 0.0042, "depth": 8}
								if obj[4]<=10:
									# {"feature": "workclass", "instances": 727, "metric_value": 0.0036, "depth": 9}
									if obj[1]<=5:
										# {"feature": "race", "instances": 702, "metric_value": 0.0014, "depth": 10}
										if obj[6]>2:
											# {"feature": "native-country", "instances": 634, "metric_value": 0.0014, "depth": 11}
											if obj[11]>10:
												# {"feature": "gender", "instances": 615, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.06341463414634146
											elif obj[11]<=10:
												# {"feature": "gender", "instances": 19, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.15789473684210525
											else: return 0.15789473684210525
										elif obj[6]<=2:
											# {"feature": "native-country", "instances": 68, "metric_value": 0.0401, "depth": 11}
											if obj[11]>37:
												# {"feature": "gender", "instances": 54, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.14814814814814814
											elif obj[11]<=37:
												return 0
											else: return 0.0
										else: return 0.11764705882352941
									elif obj[1]>5:
										# {"feature": "race", "instances": 25, "metric_value": 0.0352, "depth": 10}
										if obj[6]>2:
											# {"feature": "native-country", "instances": 22, "metric_value": 0.0141, "depth": 11}
											if obj[11]>1:
												# {"feature": "gender", "instances": 21, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.2857142857142857
											elif obj[11]<=1:
												return 0
											else: return 0.0
										elif obj[6]<=2:
											return 0
										else: return 0.0
									else: return 0.24
								elif obj[4]>10:
									# {"feature": "race", "instances": 189, "metric_value": 0.015, "depth": 9}
									if obj[6]>2:
										# {"feature": "workclass", "instances": 176, "metric_value": 0.0102, "depth": 10}
										if obj[1]<=6:
											# {"feature": "native-country", "instances": 168, "metric_value": 0.011, "depth": 11}
											if obj[11]>25:
												# {"feature": "gender", "instances": 160, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.18125
											elif obj[11]<=25:
												return 0
											else: return 0.0
										elif obj[1]>6:
											return 0
										else: return 0.0
									elif obj[6]<=2:
										return 0
									else: return 0.0
								else: return 0.15343915343915343
							elif obj[0]<=23.049242554348005:
								return 0
							else: return 0.0
						elif obj[9]>742.0390775674279:
							# {"feature": "occupation", "instances": 31, "metric_value": 0.0505, "depth": 7}
							if obj[4]>2:
								# {"feature": "workclass", "instances": 27, "metric_value": 0.0469, "depth": 8}
								if obj[1]<=3:
									# {"feature": "age", "instances": 25, "metric_value": 0.031, "depth": 9}
									if obj[0]>23:
										# {"feature": "native-country", "instances": 23, "metric_value": 0.0178, "depth": 10}
										if obj[11]>25:
											# {"feature": "race", "instances": 22, "metric_value": 0.0193, "depth": 11}
											if obj[6]>2:
												# {"feature": "gender", "instances": 21, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.42857142857142855
											elif obj[6]<=2:
												return 0
											else: return 0.0
										elif obj[11]<=25:
											return 0
										else: return 0.0
									elif obj[0]<=23:
										return 0
									else: return 0.0
								elif obj[1]>3:
									return 1
								else: return 1.0
							elif obj[4]<=2:
								return 0
							else: return 0.0
						else: return 0.3548387096774194
					else: return 0.09746192893401015
				elif obj[5]>0:
					# {"feature": "occupation", "instances": 7064, "metric_value": 0.003, "depth": 5}
					if obj[4]>3:
						# {"feature": "capital-loss", "instances": 4080, "metric_value": 0.0028, "depth": 6}
						if obj[9]<=1032.3930860577466:
							# {"feature": "gender", "instances": 3960, "metric_value": 0.0017, "depth": 7}
							if obj[7]<=0:
								# {"feature": "race", "instances": 2709, "metric_value": 0.0021, "depth": 8}
								if obj[6]>3:
									# {"feature": "workclass", "instances": 2197, "metric_value": 0.0017, "depth": 9}
									if obj[1]<=5:
										# {"feature": "age", "instances": 2152, "metric_value": 0.0013, "depth": 10}
										if obj[0]>29.426506709684077:
											# {"feature": "native-country", "instances": 1773, "metric_value": 0.0014, "depth": 11}
											if obj[11]>1:
												# {"feature": "hours-per-week", "instances": 1760, "metric_value": 0.0005, "depth": 12}
												if obj[10]>1:
													return 0
												elif obj[10]<=1:
													return 0
												else: return 0.0
											elif obj[11]<=1:
												# {"feature": "hours-per-week", "instances": 13, "metric_value": 0.0652, "depth": 12}
												if obj[10]>25:
													return 0
												elif obj[10]<=25:
													return 0
												else: return 0.0
											else: return 0.38461538461538464
										elif obj[0]<=29.426506709684077:
											# {"feature": "hours-per-week", "instances": 379, "metric_value": 0.0135, "depth": 11}
											if obj[10]>36.21899736147757:
												# {"feature": "native-country", "instances": 230, "metric_value": 0.0077, "depth": 12}
												if obj[11]>23:
													return 0
												elif obj[11]<=23:
													return 0
												else: return 0.0
											elif obj[10]<=36.21899736147757:
												# {"feature": "native-country", "instances": 149, "metric_value": 0.0117, "depth": 12}
												if obj[11]>26:
													return 0
												elif obj[11]<=26:
													return 0
												else: return 0.14285714285714285
											else: return 0.020134228187919462
										else: return 0.0633245382585752
									elif obj[1]>5:
										# {"feature": "age", "instances": 45, "metric_value": 0.021, "depth": 10}
										if obj[0]<=52.33710715471827:
											# {"feature": "native-country", "instances": 38, "metric_value": 0.0209, "depth": 11}
											if obj[11]>30:
												# {"feature": "hours-per-week", "instances": 35, "metric_value": 0.0271, "depth": 12}
												if obj[10]>20:
													return 0
												elif obj[10]<=20:
													return 1
												else: return 1.0
											elif obj[11]<=30:
												return 0
											else: return 0.0
										elif obj[0]>52.33710715471827:
											# {"feature": "hours-per-week", "instances": 7, "metric_value": 0.1449, "depth": 11}
											if obj[10]<=40:
												# {"feature": "native-country", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.4
											elif obj[10]>40:
												return 1
											else: return 1.0
										else: return 0.5714285714285714
									else: return 0.26666666666666666
								elif obj[6]<=3:
									# {"feature": "workclass", "instances": 512, "metric_value": 0.0055, "depth": 9}
									if obj[1]<=3:
										# {"feature": "age", "instances": 446, "metric_value": 0.0029, "depth": 10}
										if obj[0]<=65.03103866224686:
											# {"feature": "native-country", "instances": 434, "metric_value": 0.0023, "depth": 11}
											if obj[11]>26.194181942601695:
												# {"feature": "hours-per-week", "instances": 387, "metric_value": 0.0028, "depth": 12}
												if obj[10]>5.164742460389725:
													return 0
												elif obj[10]<=5.164742460389725:
													return 0
												else: return 0.25
											elif obj[11]<=26.194181942601695:
												# {"feature": "hours-per-week", "instances": 47, "metric_value": 0.0374, "depth": 12}
												if obj[10]<=48:
													return 0
												elif obj[10]>48:
													return 1
												else: return 1.0
											else: return 0.0851063829787234
										elif obj[0]>65.03103866224686:
											return 0
										else: return 0.0
									elif obj[1]>3:
										# {"feature": "native-country", "instances": 66, "metric_value": 0.0443, "depth": 10}
										if obj[11]>29:
											# {"feature": "age", "instances": 62, "metric_value": 0.025, "depth": 11}
											if obj[0]<=54.96677172424939:
												# {"feature": "hours-per-week", "instances": 52, "metric_value": 0.0195, "depth": 12}
												if obj[10]>25:
													return 0
												elif obj[10]<=25:
													return 0
												else: return 0.0
											elif obj[0]>54.96677172424939:
												return 0
											else: return 0.0
										elif obj[11]<=29:
											return 0.75
										else: return 0.75
									else: return 0.12121212121212122
								else: return 0.052734375
							elif obj[7]>0:
								# {"feature": "hours-per-week", "instances": 1251, "metric_value": 0.008, "depth": 8}
								if obj[10]<=42.548361310951236:
									# {"feature": "age", "instances": 851, "metric_value": 0.0036, "depth": 9}
									if obj[0]>30.026530063866034:
										# {"feature": "workclass", "instances": 691, "metric_value": 0.0019, "depth": 10}
										if obj[1]<=3:
											# {"feature": "native-country", "instances": 595, "metric_value": 0.0022, "depth": 11}
											if obj[11]>8:
												# {"feature": "race", "instances": 582, "metric_value": 0.0019, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 0
												else: return 0.11764705882352941
											elif obj[11]<=8:
												return 0
											else: return 0.0
										elif obj[1]>3:
											# {"feature": "race", "instances": 96, "metric_value": 0.0412, "depth": 11}
											if obj[6]>3:
												# {"feature": "native-country", "instances": 70, "metric_value": 0.0097, "depth": 12}
												if obj[11]>31:
													return 0
												elif obj[11]<=31:
													return 0
												else: return 0.0
											elif obj[6]<=3:
												return 0
											else: return 0.0
										else: return 0.07291666666666667
									elif obj[0]<=30.026530063866034:
										# {"feature": "native-country", "instances": 160, "metric_value": 0.0139, "depth": 10}
										if obj[11]>25:
											# {"feature": "race", "instances": 147, "metric_value": 0.0074, "depth": 11}
											if obj[6]>3:
												# {"feature": "workclass", "instances": 122, "metric_value": 0.0058, "depth": 12}
												if obj[1]<=2:
													return 0
												elif obj[1]>2:
													return 0
												else: return 0.0
											elif obj[6]<=3:
												return 0
											else: return 0.0
										elif obj[11]<=25:
											# {"feature": "race", "instances": 13, "metric_value": 0.0232, "depth": 11}
											if obj[6]>3:
												# {"feature": "workclass", "instances": 11, "metric_value": 0.0, "depth": 12}
												if obj[1]<=2:
													return 0
												else: return 0.09090909090909091
											elif obj[6]<=3:
												return 0
											else: return 0.0
										else: return 0.07692307692307693
									else: return 0.0125
								elif obj[10]>42.548361310951236:
									# {"feature": "age", "instances": 400, "metric_value": 0.0091, "depth": 9}
									if obj[0]>30.886702917532787:
										# {"feature": "native-country", "instances": 343, "metric_value": 0.0074, "depth": 10}
										if obj[11]>32:
											# {"feature": "race", "instances": 329, "metric_value": 0.0028, "depth": 11}
											if obj[6]>0:
												# {"feature": "workclass", "instances": 324, "metric_value": 0.0029, "depth": 12}
												if obj[1]<=3:
													return 0
												elif obj[1]>3:
													return 0
												else: return 0.20512820512820512
											elif obj[6]<=0:
												return 0
											else: return 0.0
										elif obj[11]<=32:
											return 0
										else: return 0.0
									elif obj[0]<=30.886702917532787:
										# {"feature": "native-country", "instances": 57, "metric_value": 0.1313, "depth": 10}
										if obj[11]>6:
											return 0
										elif obj[11]<=6:
											return 1
										else: return 1.0
									else: return 0.017543859649122806
								else: return 0.1
							else: return 0.05675459632294165
						elif obj[9]>1032.3930860577466:
							# {"feature": "gender", "instances": 120, "metric_value": 0.015, "depth": 7}
							if obj[7]<=0:
								# {"feature": "hours-per-week", "instances": 79, "metric_value": 0.0312, "depth": 8}
								if obj[10]<=50.15391568199094:
									# {"feature": "age", "instances": 72, "metric_value": 0.0207, "depth": 9}
									if obj[0]<=63.64521032101135:
										# {"feature": "workclass", "instances": 68, "metric_value": 0.0197, "depth": 10}
										if obj[1]<=5:
											# {"feature": "race", "instances": 66, "metric_value": 0.0166, "depth": 11}
											if obj[6]>2:
												# {"feature": "native-country", "instances": 56, "metric_value": 0.0072, "depth": 12}
												if obj[11]>21:
													return 0
												elif obj[11]<=21:
													return 0
												else: return 0.0
											elif obj[6]<=2:
												# {"feature": "native-country", "instances": 10, "metric_value": 0.0172, "depth": 12}
												if obj[11]>15:
													return 0
												elif obj[11]<=15:
													return 0
												else: return 0.0
											else: return 0.1
										elif obj[1]>5:
											return 1
										else: return 1.0
									elif obj[0]>63.64521032101135:
										return 0
									else: return 0.0
								elif obj[10]>50.15391568199094:
									return 0
								else: return 0.0
							elif obj[7]>0:
								# {"feature": "hours-per-week", "instances": 41, "metric_value": 0.0345, "depth": 8}
								if obj[10]<=70:
									# {"feature": "workclass", "instances": 40, "metric_value": 0.0438, "depth": 9}
									if obj[1]<=4:
										# {"feature": "age", "instances": 36, "metric_value": 0.0874, "depth": 10}
										if obj[0]<=41.388888888888886:
											return 0
										elif obj[0]>41.388888888888886:
											# {"feature": "race", "instances": 15, "metric_value": 0.0, "depth": 11}
											if obj[6]<=4:
												# {"feature": "native-country", "instances": 15, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.13333333333333333
											else: return 0.13333333333333333
										else: return 0.13333333333333333
									elif obj[1]>4:
										return 0.5
									else: return 0.5
								elif obj[10]>70:
									return 1
								else: return 1.0
							else: return 0.12195121951219512
						else: return 0.25
					elif obj[4]<=3:
						# {"feature": "gender", "instances": 2984, "metric_value": 0.0027, "depth": 6}
						if obj[7]<=0:
							# {"feature": "capital-loss", "instances": 2102, "metric_value": 0.0037, "depth": 7}
							if obj[9]<=1106.1471961105517:
								# {"feature": "age", "instances": 2030, "metric_value": 0.0017, "depth": 8}
								if obj[0]>31.158786358249344:
									# {"feature": "hours-per-week", "instances": 1651, "metric_value": 0.0015, "depth": 9}
									if obj[10]>30.777171447013878:
										# {"feature": "native-country", "instances": 1489, "metric_value": 0.0006, "depth": 10}
										if obj[11]>1:
											# {"feature": "workclass", "instances": 1482, "metric_value": 0.0006, "depth": 11}
											if obj[1]<=5:
												# {"feature": "race", "instances": 1364, "metric_value": 0.002, "depth": 12}
												if obj[6]>0:
													return 0
												elif obj[6]<=0:
													return 0
												else: return 0.0
											elif obj[1]>5:
												# {"feature": "race", "instances": 118, "metric_value": 0.0005, "depth": 12}
												if obj[6]>2:
													return 0
												elif obj[6]<=2:
													return 0
												else: return 0.225
											else: return 0.2033898305084746
										elif obj[11]<=1:
											# {"feature": "workclass", "instances": 7, "metric_value": 0.0663, "depth": 11}
											if obj[1]<=2:
												# {"feature": "race", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[6]<=4:
													return 1
												else: return 0.5
											elif obj[1]>2:
												return 0
											else: return 0.0
										else: return 0.42857142857142855
									elif obj[10]<=30.777171447013878:
										# {"feature": "race", "instances": 162, "metric_value": 0.0055, "depth": 10}
										if obj[6]>0:
											# {"feature": "workclass", "instances": 161, "metric_value": 0.0047, "depth": 11}
											if obj[1]<=6:
												# {"feature": "native-country", "instances": 150, "metric_value": 0.005, "depth": 12}
												if obj[11]>4:
													return 0
												elif obj[11]<=4:
													return 1
												else: return 0.6666666666666666
											elif obj[1]>6:
												# {"feature": "native-country", "instances": 11, "metric_value": 0.0434, "depth": 12}
												if obj[11]>2:
													return 0
												elif obj[11]<=2:
													return 0
												else: return 0.0
											else: return 0.45454545454545453
										elif obj[6]<=0:
											return 1
										else: return 1.0
									else: return 0.24074074074074073
								elif obj[0]<=31.158786358249344:
									# {"feature": "native-country", "instances": 379, "metric_value": 0.0031, "depth": 9}
									if obj[11]>13:
										# {"feature": "hours-per-week", "instances": 372, "metric_value": 0.0023, "depth": 10}
										if obj[10]>12.143130072856206:
											# {"feature": "race", "instances": 367, "metric_value": 0.0013, "depth": 11}
											if obj[6]>1:
												# {"feature": "workclass", "instances": 352, "metric_value": 0.0011, "depth": 12}
												if obj[1]<=2:
													return 0
												elif obj[1]>2:
													return 0
												else: return 0.13559322033898305
											elif obj[6]<=1:
												# {"feature": "workclass", "instances": 15, "metric_value": 0.017, "depth": 12}
												if obj[1]<=4:
													return 0
												elif obj[1]>4:
													return 0
												else: return 0.0
											else: return 0.2
										elif obj[10]<=12.143130072856206:
											return 0
										else: return 0.0
									elif obj[11]<=13:
										return 0
									else: return 0.0
								else: return 0.10026385224274406
							elif obj[9]>1106.1471961105517:
								# {"feature": "age", "instances": 72, "metric_value": 0.0115, "depth": 8}
								if obj[0]<=63.90837375366557:
									# {"feature": "hours-per-week", "instances": 70, "metric_value": 0.0086, "depth": 9}
									if obj[10]>6:
										# {"feature": "native-country", "instances": 69, "metric_value": 0.0088, "depth": 10}
										if obj[11]>2:
											# {"feature": "race", "instances": 68, "metric_value": 0.006, "depth": 11}
											if obj[6]>0:
												# {"feature": "workclass", "instances": 67, "metric_value": 0.004, "depth": 12}
												if obj[1]<=3:
													return 0
												elif obj[1]>3:
													return 0
												else: return 0.2857142857142857
											elif obj[6]<=0:
												return 0
											else: return 0.0
										elif obj[11]<=2:
											return 1
										else: return 1.0
									elif obj[10]<=6:
										return 1
									else: return 1.0
								elif obj[0]>63.90837375366557:
									return 0
								else: return 0.0
							else: return 0.4027777777777778
						elif obj[7]>0:
							# {"feature": "hours-per-week", "instances": 882, "metric_value": 0.0121, "depth": 7}
							if obj[10]<=43.14399092970522:
								# {"feature": "age", "instances": 602, "metric_value": 0.0091, "depth": 8}
								if obj[0]>40.95681063122924:
									# {"feature": "workclass", "instances": 301, "metric_value": 0.0172, "depth": 9}
									if obj[1]<=5:
										# {"feature": "native-country", "instances": 269, "metric_value": 0.0067, "depth": 10}
										if obj[11]>4:
											# {"feature": "race", "instances": 266, "metric_value": 0.0188, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 236, "metric_value": 0.0027, "depth": 12}
												if obj[9]<=1974:
													return 0
												elif obj[9]>1974:
													return 1
												else: return 0.5
											elif obj[6]<=2:
												return 0
											else: return 0.0
										elif obj[11]<=4:
											return 0.6666666666666666
										else: return 0.6666666666666666
									elif obj[1]>5:
										return 0
									else: return 0.0
								elif obj[0]<=40.95681063122924:
									# {"feature": "workclass", "instances": 301, "metric_value": 0.0142, "depth": 9}
									if obj[1]<=5:
										# {"feature": "race", "instances": 286, "metric_value": 0.0084, "depth": 10}
										if obj[6]>3:
											# {"feature": "native-country", "instances": 254, "metric_value": 0.0037, "depth": 11}
											if obj[11]>31:
												# {"feature": "capital-loss", "instances": 242, "metric_value": 0.0017, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											elif obj[11]<=31:
												return 0
											else: return 0.0
										elif obj[6]<=3:
											return 0
										else: return 0.0
									elif obj[1]>5:
										# {"feature": "race", "instances": 15, "metric_value": 0.0349, "depth": 10}
										if obj[6]>2:
											# {"feature": "native-country", "instances": 13, "metric_value": 0.0216, "depth": 11}
											if obj[11]>25:
												# {"feature": "capital-loss", "instances": 12, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.25
											elif obj[11]<=25:
												return 0
											else: return 0.0
										elif obj[6]<=2:
											return 0
										else: return 0.0
									else: return 0.2
								else: return 0.029900332225913623
							elif obj[10]>43.14399092970522:
								# {"feature": "capital-loss", "instances": 280, "metric_value": 0.012, "depth": 8}
								if obj[9]<=2339:
									# {"feature": "workclass", "instances": 277, "metric_value": 0.0084, "depth": 9}
									if obj[1]<=2:
										# {"feature": "native-country", "instances": 195, "metric_value": 0.0098, "depth": 10}
										if obj[11]>36:
											# {"feature": "age", "instances": 185, "metric_value": 0.0103, "depth": 11}
											if obj[0]<=38.84324324324324:
												# {"feature": "race", "instances": 101, "metric_value": 0.0234, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 1
												else: return 0.6666666666666666
											elif obj[0]>38.84324324324324:
												# {"feature": "race", "instances": 84, "metric_value": 0.0013, "depth": 12}
												if obj[6]>2:
													return 0
												elif obj[6]<=2:
													return 0
												else: return 0.3333333333333333
											else: return 0.19047619047619047
										elif obj[11]<=36:
											return 0
										else: return 0.0
									elif obj[1]>2:
										# {"feature": "race", "instances": 82, "metric_value": 0.0072, "depth": 10}
										if obj[6]>0:
											# {"feature": "native-country", "instances": 80, "metric_value": 0.0075, "depth": 11}
											if obj[11]>3:
												# {"feature": "age", "instances": 78, "metric_value": 0.0039, "depth": 12}
												if obj[0]>19:
													return 0
												elif obj[0]<=19:
													return 0
												else: return 0.0
											elif obj[11]<=3:
												return 0
											else: return 0.0
										elif obj[6]<=0:
											return 0
										else: return 0.0
									else: return 0.25609756097560976
								elif obj[9]>2339:
									return 1
								else: return 1.0
							else: return 0.17142857142857143
						else: return 0.09523809523809523
					else: return 0.13941018766756033
				else: return 0.10801245753114383
			elif obj[8]>6082.379545993911:
				# {"feature": "relationship", "instances": 748, "metric_value": 0.0205, "depth": 4}
				if obj[5]<=0:
					# {"feature": "age", "instances": 579, "metric_value": 0.0499, "depth": 5}
					if obj[0]<=58.93310665460399:
						# {"feature": "race", "instances": 476, "metric_value": 0.0402, "depth": 6}
						if obj[6]>1:
							return 1
						elif obj[6]<=1:
							# {"feature": "hours-per-week", "instances": 8, "metric_value": 0.3307, "depth": 7}
							if obj[10]<=75:
								return 1
							elif obj[10]>75:
								return 0
							else: return 0.0
						else: return 0.875
					elif obj[0]>58.93310665460399:
						# {"feature": "hours-per-week", "instances": 103, "metric_value": 0.0144, "depth": 6}
						if obj[10]>6:
							# {"feature": "occupation", "instances": 102, "metric_value": 0.0106, "depth": 7}
							if obj[4]>3:
								# {"feature": "native-country", "instances": 59, "metric_value": 0.0102, "depth": 8}
								if obj[11]>29:
									# {"feature": "race", "instances": 56, "metric_value": 0.0082, "depth": 9}
									if obj[6]>2:
										# {"feature": "workclass", "instances": 54, "metric_value": 0.009, "depth": 10}
										if obj[1]<=3:
											# {"feature": "gender", "instances": 47, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 47, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.8936170212765957
											else: return 0.8936170212765957
										elif obj[1]>3:
											# {"feature": "gender", "instances": 7, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7142857142857143
											else: return 0.7142857142857143
										else: return 0.7142857142857143
									elif obj[6]<=2:
										return 0.5
									else: return 0.5
								elif obj[11]<=29:
									return 1
								else: return 1.0
							elif obj[4]<=3:
								# {"feature": "workclass", "instances": 43, "metric_value": 0.0461, "depth": 8}
								if obj[1]<=3:
									# {"feature": "native-country", "instances": 27, "metric_value": 0.0107, "depth": 9}
									if obj[11]>30:
										# {"feature": "race", "instances": 25, "metric_value": 0.006, "depth": 10}
										if obj[6]>1:
											# {"feature": "gender", "instances": 24, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 24, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9166666666666666
											else: return 0.9166666666666666
										elif obj[6]<=1:
											return 1
										else: return 1.0
									elif obj[11]<=30:
										return 1
									else: return 1.0
								elif obj[1]>3:
									return 1
								else: return 1.0
							else: return 0.9534883720930233
						elif obj[10]<=6:
							return 0
						else: return 0.0
					else: return 0.8932038834951457
				elif obj[5]>0:
					# {"feature": "occupation", "instances": 169, "metric_value": 0.012, "depth": 5}
					if obj[4]<=12:
						# {"feature": "hours-per-week", "instances": 164, "metric_value": 0.0076, "depth": 6}
						if obj[10]>18.17908388509196:
							# {"feature": "age", "instances": 157, "metric_value": 0.0046, "depth": 7}
							if obj[0]<=67.49845033601565:
								# {"feature": "native-country", "instances": 153, "metric_value": 0.0034, "depth": 8}
								if obj[11]>25:
									# {"feature": "race", "instances": 146, "metric_value": 0.0025, "depth": 9}
									if obj[6]>2:
										# {"feature": "workclass", "instances": 130, "metric_value": 0.0022, "depth": 10}
										if obj[1]<=5:
											# {"feature": "gender", "instances": 119, "metric_value": 0.0044, "depth": 11}
											if obj[7]<=0:
												# {"feature": "capital-loss", "instances": 83, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.927710843373494
											elif obj[7]>0:
												# {"feature": "capital-loss", "instances": 36, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.8611111111111112
											else: return 0.8611111111111112
										elif obj[1]>5:
											# {"feature": "gender", "instances": 11, "metric_value": 0.0455, "depth": 11}
											if obj[7]<=0:
												# {"feature": "capital-loss", "instances": 9, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7777777777777778
											elif obj[7]>0:
												return 1
											else: return 1.0
										else: return 0.8181818181818182
									elif obj[6]<=2:
										# {"feature": "gender", "instances": 16, "metric_value": 0.1039, "depth": 10}
										if obj[7]<=0:
											# {"feature": "workclass", "instances": 10, "metric_value": 0.071, "depth": 11}
											if obj[1]<=4:
												# {"feature": "capital-loss", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.625
											elif obj[1]>4:
												return 1
											else: return 1.0
										elif obj[7]>0:
											return 1
										else: return 1.0
									else: return 0.8125
								elif obj[11]<=25:
									# {"feature": "workclass", "instances": 7, "metric_value": 0.166, "depth": 9}
									if obj[1]<=2:
										return 0.5
									elif obj[1]>2:
										return 1
									else: return 1.0
								else: return 0.7142857142857143
							elif obj[0]>67.49845033601565:
								return 1
							else: return 1.0
						elif obj[10]<=18.17908388509196:
							return 1
						else: return 1.0
					elif obj[4]>12:
						# {"feature": "age", "instances": 5, "metric_value": 0.1435, "depth": 6}
						if obj[0]>36:
							return 0.25
						elif obj[0]<=36:
							return 1
						else: return 1.0
					else: return 0.4
				else: return 0.8757396449704142
			else: return 0.9558823529411765
		elif obj[2]>12:
			# {"feature": "capital-gain", "instances": 8010, "metric_value": 0.0235, "depth": 3}
			if obj[8]<=3553.565418227216:
				# {"feature": "relationship", "instances": 6776, "metric_value": 0.019, "depth": 4}
				if obj[5]<=0:
					# {"feature": "capital-loss", "instances": 4930, "metric_value": 0.0125, "depth": 5}
					if obj[9]<=1485.1361912827774:
						# {"feature": "hours-per-week", "instances": 4383, "metric_value": 0.0101, "depth": 6}
						if obj[10]>33.01713779773306:
							# {"feature": "age", "instances": 4049, "metric_value": 0.0053, "depth": 7}
							if obj[0]>33.006456566546696:
								# {"feature": "occupation", "instances": 3302, "metric_value": 0.002, "depth": 8}
								if obj[4]>2:
									# {"feature": "workclass", "instances": 2992, "metric_value": 0.0013, "depth": 9}
									if obj[1]<=5:
										# {"feature": "race", "instances": 2594, "metric_value": 0.0006, "depth": 10}
										if obj[6]>3:
											# {"feature": "native-country", "instances": 2369, "metric_value": 0.0005, "depth": 11}
											if obj[11]>36.90291262135922:
												# {"feature": "gender", "instances": 2263, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.7193990278391516
											elif obj[11]<=36.90291262135922:
												# {"feature": "gender", "instances": 106, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6226415094339622
											else: return 0.6226415094339622
										elif obj[6]<=3:
											# {"feature": "native-country", "instances": 225, "metric_value": 0.0059, "depth": 11}
											if obj[11]<=38:
												# {"feature": "gender", "instances": 223, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6412556053811659
											elif obj[11]>38:
												return 0
											else: return 0.0
										else: return 0.6355555555555555
									elif obj[1]>5:
										# {"feature": "race", "instances": 398, "metric_value": 0.0025, "depth": 10}
										if obj[6]>0:
											# {"feature": "native-country", "instances": 397, "metric_value": 0.0025, "depth": 11}
											if obj[11]>1:
												# {"feature": "gender", "instances": 396, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.797979797979798
											elif obj[11]<=1:
												return 0
											else: return 0.0
										elif obj[6]<=0:
											return 0
										else: return 0.0
									else: return 0.7939698492462312
								elif obj[4]<=2:
									# {"feature": "workclass", "instances": 310, "metric_value": 0.0043, "depth": 9}
									if obj[1]<=6:
										# {"feature": "native-country", "instances": 296, "metric_value": 0.0041, "depth": 10}
										if obj[11]<=38:
											# {"feature": "race", "instances": 294, "metric_value": 0.0014, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 293, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5972696245733788
											elif obj[6]<=0:
												return 1
											else: return 1.0
										elif obj[11]>38:
											return 0
										else: return 0.0
									elif obj[1]>6:
										# {"feature": "race", "instances": 14, "metric_value": 0.0232, "depth": 10}
										if obj[6]>2:
											# {"feature": "gender", "instances": 13, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "native-country", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.3076923076923077
											else: return 0.3076923076923077
										elif obj[6]<=2:
											return 0
										else: return 0.0
									else: return 0.2857142857142857
								else: return 0.5806451612903226
							elif obj[0]<=33.006456566546696:
								# {"feature": "native-country", "instances": 747, "metric_value": 0.003, "depth": 8}
								if obj[11]>35.967871485943775:
									# {"feature": "race", "instances": 680, "metric_value": 0.0017, "depth": 9}
									if obj[6]>1:
										# {"feature": "occupation", "instances": 668, "metric_value": 0.0015, "depth": 10}
										if obj[4]>3:
											# {"feature": "workclass", "instances": 447, "metric_value": 0.0012, "depth": 11}
											if obj[1]<=5:
												# {"feature": "gender", "instances": 421, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5083135391923991
											elif obj[1]>5:
												# {"feature": "gender", "instances": 26, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6538461538461539
											else: return 0.6538461538461539
										elif obj[4]<=3:
											# {"feature": "workclass", "instances": 221, "metric_value": 0.0033, "depth": 11}
											if obj[1]<=2:
												# {"feature": "gender", "instances": 174, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6264367816091954
											elif obj[1]>2:
												# {"feature": "gender", "instances": 47, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.48936170212765956
											else: return 0.48936170212765956
										else: return 0.5972850678733032
									elif obj[6]<=1:
										# {"feature": "occupation", "instances": 12, "metric_value": 0.0393, "depth": 10}
										if obj[4]>5:
											# {"feature": "workclass", "instances": 10, "metric_value": 0.1586, "depth": 11}
											if obj[1]<=2:
												return 1
											elif obj[1]>2:
												return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[4]<=5:
											return 0.5
										else: return 0.5
									else: return 0.8333333333333334
								elif obj[11]<=35.967871485943775:
									# {"feature": "occupation", "instances": 67, "metric_value": 0.0155, "depth": 9}
									if obj[4]>3:
										# {"feature": "workclass", "instances": 44, "metric_value": 0.0388, "depth": 10}
										if obj[1]<=6:
											# {"feature": "race", "instances": 42, "metric_value": 0.0019, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 24, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.20833333333333334
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 18, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.2777777777777778
											else: return 0.2777777777777778
										elif obj[1]>6:
											return 1
										else: return 1.0
									elif obj[4]<=3:
										# {"feature": "workclass", "instances": 23, "metric_value": 0.0735, "depth": 10}
										if obj[1]<=2:
											# {"feature": "race", "instances": 20, "metric_value": 0.0005, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.6153846153846154
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5714285714285714
											else: return 0.5714285714285714
										elif obj[1]>2:
											return 0
										else: return 0.0
									else: return 0.5217391304347826
								else: return 0.3582089552238806
							else: return 0.5314591700133868
						elif obj[10]<=33.01713779773306:
							# {"feature": "occupation", "instances": 334, "metric_value": 0.0141, "depth": 7}
							if obj[4]>7:
								# {"feature": "age", "instances": 240, "metric_value": 0.0096, "depth": 8}
								if obj[0]>38.49359778559699:
									# {"feature": "native-country", "instances": 186, "metric_value": 0.0097, "depth": 9}
									if obj[11]>30:
										# {"feature": "race", "instances": 183, "metric_value": 0.0045, "depth": 10}
										if obj[6]>1:
											# {"feature": "workclass", "instances": 181, "metric_value": 0.0011, "depth": 11}
											if obj[1]<=6:
												# {"feature": "gender", "instances": 172, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.4011627906976744
											elif obj[1]>6:
												# {"feature": "gender", "instances": 9, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.5555555555555556
											else: return 0.5555555555555556
										elif obj[6]<=1:
											return 0
										else: return 0.0
									elif obj[11]<=30:
										return 1
									else: return 1.0
								elif obj[0]<=38.49359778559699:
									# {"feature": "workclass", "instances": 54, "metric_value": 0.1019, "depth": 9}
									if obj[1]<=3:
										# {"feature": "native-country", "instances": 35, "metric_value": 0.0152, "depth": 10}
										if obj[11]>18:
											# {"feature": "race", "instances": 30, "metric_value": 0.0102, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 29, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.27586206896551724
											elif obj[6]<=1:
												return 0
											else: return 0.0
										elif obj[11]<=18:
											# {"feature": "race", "instances": 5, "metric_value": 0.0899, "depth": 11}
											if obj[6]>1:
												return 0.5
											elif obj[6]<=1:
												return 1
											else: return 1.0
										else: return 0.6
									elif obj[1]>3:
										return 0
									else: return 0.0
								else: return 0.2037037037037037
							elif obj[4]<=7:
								# {"feature": "workclass", "instances": 94, "metric_value": 0.0326, "depth": 8}
								if obj[1]<=3:
									# {"feature": "native-country", "instances": 80, "metric_value": 0.0269, "depth": 9}
									if obj[11]>30:
										# {"feature": "age", "instances": 71, "metric_value": 0.0076, "depth": 10}
										if obj[0]>54.11267605633803:
											# {"feature": "race", "instances": 40, "metric_value": 0.0073, "depth": 11}
											if obj[6]>2:
												# {"feature": "gender", "instances": 39, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.2564102564102564
											elif obj[6]<=2:
												return 0
											else: return 0.0
										elif obj[0]<=54.11267605633803:
											# {"feature": "race", "instances": 31, "metric_value": 0.0063, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 30, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 0
												else: return 0.13333333333333333
											elif obj[6]<=1:
												return 0
											else: return 0.0
										else: return 0.12903225806451613
									elif obj[11]<=30:
										return 0
									else: return 0.0
								elif obj[1]>3:
									return 0
								else: return 0.0
							else: return 0.14893617021276595
						else: return 0.30538922155688625
					elif obj[9]>1485.1361912827774:
						# {"feature": "hours-per-week", "instances": 547, "metric_value": 0.0084, "depth": 6}
						if obj[10]>35.94570933054896:
							# {"feature": "occupation", "instances": 514, "metric_value": 0.0035, "depth": 7}
							if obj[4]>2:
								# {"feature": "age", "instances": 486, "metric_value": 0.0032, "depth": 8}
								if obj[0]>34.35156414794345:
									# {"feature": "native-country", "instances": 402, "metric_value": 0.0019, "depth": 9}
									if obj[11]>2:
										# {"feature": "race", "instances": 398, "metric_value": 0.0076, "depth": 10}
										if obj[6]>2:
											# {"feature": "workclass", "instances": 372, "metric_value": 0.0016, "depth": 11}
											if obj[1]<=2:
												# {"feature": "gender", "instances": 209, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.9569377990430622
											elif obj[1]>2:
												# {"feature": "gender", "instances": 163, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.9325153374233128
											else: return 0.9325153374233128
										elif obj[6]<=2:
											return 1
										else: return 1.0
									elif obj[11]<=2:
										return 0.75
									else: return 0.75
								elif obj[0]<=34.35156414794345:
									# {"feature": "workclass", "instances": 84, "metric_value": 0.0216, "depth": 9}
									if obj[1]<=3:
										# {"feature": "native-country", "instances": 71, "metric_value": 0.0106, "depth": 10}
										if obj[11]>13:
											# {"feature": "race", "instances": 68, "metric_value": 0.0113, "depth": 11}
											if obj[6]>3:
												# {"feature": "gender", "instances": 62, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.9354838709677419
											elif obj[6]<=3:
												return 1
											else: return 1.0
										elif obj[11]<=13:
											return 0.6666666666666666
										else: return 0.6666666666666666
									elif obj[1]>3:
										# {"feature": "race", "instances": 13, "metric_value": 0.0618, "depth": 10}
										if obj[6]>1:
											# {"feature": "native-country", "instances": 12, "metric_value": 0.0248, "depth": 11}
											if obj[11]>10:
												# {"feature": "gender", "instances": 11, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.7272727272727273
											elif obj[11]<=10:
												return 1
											else: return 1.0
										elif obj[6]<=1:
											return 0
										else: return 0.0
									else: return 0.6923076923076923
								else: return 0.8928571428571429
							elif obj[4]<=2:
								# {"feature": "age", "instances": 28, "metric_value": 0.0259, "depth": 8}
								if obj[0]>30:
									# {"feature": "native-country", "instances": 25, "metric_value": 0.0113, "depth": 9}
									if obj[11]>24:
										# {"feature": "race", "instances": 23, "metric_value": 0.0205, "depth": 10}
										if obj[6]>1:
											# {"feature": "workclass", "instances": 21, "metric_value": 0.0117, "depth": 11}
											if obj[1]<=6:
												# {"feature": "gender", "instances": 20, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.8
											elif obj[1]>6:
												return 1
											else: return 1.0
										elif obj[6]<=1:
											return 1
										else: return 1.0
									elif obj[11]<=24:
										return 0.5
									else: return 0.5
								elif obj[0]<=30:
									return 1
								else: return 1.0
							else: return 0.8214285714285714
						elif obj[10]<=35.94570933054896:
							# {"feature": "age", "instances": 33, "metric_value": 0.0705, "depth": 7}
							if obj[0]<=69.90537821928608:
								# {"feature": "occupation", "instances": 26, "metric_value": 0.0289, "depth": 8}
								if obj[4]<=11:
									# {"feature": "workclass", "instances": 24, "metric_value": 0.0164, "depth": 9}
									if obj[1]<=4:
										# {"feature": "native-country", "instances": 23, "metric_value": 0.0178, "depth": 10}
										if obj[11]>2:
											# {"feature": "race", "instances": 22, "metric_value": 0.0108, "depth": 11}
											if obj[6]>3:
												# {"feature": "gender", "instances": 19, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 1
												else: return 0.631578947368421
											elif obj[6]<=3:
												return 0.3333333333333333
											else: return 0.3333333333333333
										elif obj[11]<=2:
											return 1
										else: return 1.0
									elif obj[1]>4:
										return 1
									else: return 1.0
								elif obj[4]>11:
									return 1
								else: return 1.0
							elif obj[0]>69.90537821928608:
								return 1
							else: return 1.0
						else: return 0.7272727272727273
					else: return 0.9195612431444241
				elif obj[5]>0:
					# {"feature": "capital-loss", "instances": 1846, "metric_value": 0.0087, "depth": 5}
					if obj[9]<=1792.8792062725402:
						# {"feature": "hours-per-week", "instances": 1739, "metric_value": 0.0047, "depth": 6}
						if obj[10]<=41.19206440483036:
							# {"feature": "gender", "instances": 1134, "metric_value": 0.0083, "depth": 7}
							if obj[7]<=0:
								# {"feature": "occupation", "instances": 878, "metric_value": 0.002, "depth": 8}
								if obj[4]>2:
									# {"feature": "age", "instances": 742, "metric_value": 0.0021, "depth": 9}
									if obj[0]<=53.17981399758544:
										# {"feature": "race", "instances": 628, "metric_value": 0.0006, "depth": 10}
										if obj[6]>3:
											# {"feature": "workclass", "instances": 518, "metric_value": 0.0009, "depth": 11}
											if obj[1]<=5:
												# {"feature": "native-country", "instances": 504, "metric_value": 0.0005, "depth": 12}
												if obj[11]>4:
													return 0
												elif obj[11]<=4:
													return 1
												else: return 0.6666666666666666
											elif obj[1]>5:
												# {"feature": "native-country", "instances": 14, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 1
												else: return 0.5714285714285714
											else: return 0.5714285714285714
										elif obj[6]<=3:
											# {"feature": "native-country", "instances": 110, "metric_value": 0.0032, "depth": 11}
											if obj[11]<=38:
												# {"feature": "workclass", "instances": 109, "metric_value": 0.0005, "depth": 12}
												if obj[1]<=5:
													return 0
												elif obj[1]>5:
													return 0
												else: return 0.2727272727272727
											elif obj[11]>38:
												return 0
											else: return 0.0
										else: return 0.32727272727272727
									elif obj[0]>53.17981399758544:
										# {"feature": "race", "instances": 114, "metric_value": 0.0053, "depth": 10}
										if obj[6]>1:
											# {"feature": "native-country", "instances": 112, "metric_value": 0.0054, "depth": 11}
											if obj[11]>4:
												# {"feature": "workclass", "instances": 110, "metric_value": 0.0016, "depth": 12}
												if obj[1]<=3:
													return 0
												elif obj[1]>3:
													return 0
												else: return 0.3170731707317073
											elif obj[11]<=4:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 0
										else: return 0.0
									else: return 0.2631578947368421
								elif obj[4]<=2:
									# {"feature": "native-country", "instances": 136, "metric_value": 0.0064, "depth": 9}
									if obj[11]>4:
										# {"feature": "race", "instances": 135, "metric_value": 0.0042, "depth": 10}
										if obj[6]>0:
											# {"feature": "age", "instances": 133, "metric_value": 0.0038, "depth": 11}
											if obj[0]<=42.26315789473684:
												# {"feature": "workclass", "instances": 80, "metric_value": 0.004, "depth": 12}
												if obj[1]<=6:
													return 0
												elif obj[1]>6:
													return 0
												else: return 0.0
											elif obj[0]>42.26315789473684:
												# {"feature": "workclass", "instances": 53, "metric_value": 0.0201, "depth": 12}
												if obj[1]<=6:
													return 0
												elif obj[1]>6:
													return 1
												else: return 1.0
											else: return 0.18867924528301888
										elif obj[6]<=0:
											return 0
										else: return 0.0
									elif obj[11]<=4:
										return 1
									else: return 1.0
								else: return 0.25
							elif obj[7]>0:
								# {"feature": "age", "instances": 256, "metric_value": 0.0079, "depth": 8}
								if obj[0]<=65.31882163804615:
									# {"feature": "race", "instances": 247, "metric_value": 0.0056, "depth": 9}
									if obj[6]>3:
										# {"feature": "workclass", "instances": 215, "metric_value": 0.0056, "depth": 10}
										if obj[1]<=6:
											# {"feature": "occupation", "instances": 210, "metric_value": 0.0046, "depth": 11}
											if obj[4]<=12:
												# {"feature": "native-country", "instances": 206, "metric_value": 0.0043, "depth": 12}
												if obj[11]>1:
													return 0
												elif obj[11]<=1:
													return 1
												else: return 0.6666666666666666
											elif obj[4]>12:
												return 0
											else: return 0.0
										elif obj[1]>6:
											return 0
										else: return 0.0
									elif obj[6]<=3:
										# {"feature": "workclass", "instances": 32, "metric_value": 0.0709, "depth": 10}
										if obj[1]<=2:
											# {"feature": "occupation", "instances": 17, "metric_value": 0.0869, "depth": 11}
											if obj[4]>7:
												# {"feature": "native-country", "instances": 10, "metric_value": 0.0354, "depth": 12}
												if obj[11]>18:
													return 0
												elif obj[11]<=18:
													return 1
												else: return 0.5
											elif obj[4]<=7:
												return 0
											else: return 0.0
										elif obj[1]>2:
											return 0
										else: return 0.0
									else: return 0.0625
								elif obj[0]>65.31882163804615:
									return 0
								else: return 0.0
							else: return 0.1640625
						elif obj[10]>41.19206440483036:
							# {"feature": "occupation", "instances": 605, "metric_value": 0.0044, "depth": 7}
							if obj[4]<=12:
								# {"feature": "age", "instances": 599, "metric_value": 0.0027, "depth": 8}
								if obj[0]<=61.33888163213689:
									# {"feature": "workclass", "instances": 585, "metric_value": 0.0028, "depth": 9}
									if obj[1]<=4:
										# {"feature": "native-country", "instances": 494, "metric_value": 0.001, "depth": 10}
										if obj[11]>8:
											# {"feature": "gender", "instances": 483, "metric_value": 0.0013, "depth": 11}
											if obj[7]<=0:
												# {"feature": "race", "instances": 305, "metric_value": 0.0036, "depth": 12}
												if obj[6]>0:
													return 0
												elif obj[6]<=0:
													return 1
												else: return 1.0
											elif obj[7]>0:
												# {"feature": "race", "instances": 178, "metric_value": 0.0006, "depth": 12}
												if obj[6]>2:
													return 0
												elif obj[6]<=2:
													return 0
												else: return 0.46153846153846156
											else: return 0.37640449438202245
										elif obj[11]<=8:
											# {"feature": "gender", "instances": 11, "metric_value": 0.1661, "depth": 11}
											if obj[7]<=0:
												# {"feature": "race", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[6]<=4:
													return 0
												else: return 0.42857142857142855
											elif obj[7]>0:
												return 1
											else: return 1.0
										else: return 0.6363636363636364
									elif obj[1]>4:
										# {"feature": "native-country", "instances": 91, "metric_value": 0.0048, "depth": 10}
										if obj[11]>9:
											# {"feature": "race", "instances": 90, "metric_value": 0.004, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 84, "metric_value": 0.0006, "depth": 12}
												if obj[7]<=0:
													return 1
												elif obj[7]>0:
													return 1
												else: return 0.6111111111111112
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.3333333333333333
											else: return 0.3333333333333333
										elif obj[11]<=9:
											return 1
										else: return 1.0
									else: return 0.5714285714285714
								elif obj[0]>61.33888163213689:
									# {"feature": "native-country", "instances": 14, "metric_value": 0.1025, "depth": 9}
									if obj[11]>4:
										# {"feature": "workclass", "instances": 13, "metric_value": 0.1577, "depth": 10}
										if obj[1]<=6:
											return 0
										elif obj[1]>6:
											return 0.3333333333333333
										else: return 0.3333333333333333
									elif obj[11]<=4:
										return 1
									else: return 1.0
								else: return 0.14285714285714285
							elif obj[4]>12:
								return 0
							else: return 0.0
						else: return 0.4380165289256198
					elif obj[9]>1792.8792062725402:
						# {"feature": "race", "instances": 107, "metric_value": 0.0288, "depth": 6}
						if obj[6]>2:
							# {"feature": "age", "instances": 97, "metric_value": 0.0175, "depth": 7}
							if obj[0]<=52.92107137034671:
								# {"feature": "hours-per-week", "instances": 81, "metric_value": 0.0357, "depth": 8}
								if obj[10]>29.27691361011834:
									# {"feature": "gender", "instances": 71, "metric_value": 0.028, "depth": 9}
									if obj[7]<=0:
										# {"feature": "occupation", "instances": 51, "metric_value": 0.0231, "depth": 10}
										if obj[4]>3:
											# {"feature": "workclass", "instances": 33, "metric_value": 0.011, "depth": 11}
											if obj[1]<=2:
												# {"feature": "native-country", "instances": 18, "metric_value": 0.0126, "depth": 12}
												if obj[11]>15:
													return 1
												elif obj[11]<=15:
													return 1
												else: return 1.0
											elif obj[1]>2:
												# {"feature": "native-country", "instances": 15, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 1
												else: return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[4]<=3:
											# {"feature": "workclass", "instances": 18, "metric_value": 0.0448, "depth": 11}
											if obj[1]<=2:
												# {"feature": "native-country", "instances": 12, "metric_value": 0.0129, "depth": 12}
												if obj[11]>8:
													return 1
												elif obj[11]<=8:
													return 1
												else: return 1.0
											elif obj[1]>2:
												return 1
											else: return 1.0
										else: return 0.9444444444444444
									elif obj[7]>0:
										# {"feature": "occupation", "instances": 20, "metric_value": 0.0817, "depth": 10}
										if obj[4]>2:
											# {"feature": "workclass", "instances": 17, "metric_value": 0.0373, "depth": 11}
											if obj[1]<=3:
												# {"feature": "native-country", "instances": 13, "metric_value": 0.0618, "depth": 12}
												if obj[11]>5:
													return 1
												elif obj[11]<=5:
													return 0
												else: return 0.0
											elif obj[1]>3:
												return 0.25
											else: return 0.25
										elif obj[4]<=2:
											return 0
										else: return 0.0
									else: return 0.5
								elif obj[10]<=29.27691361011834:
									return 1
								else: return 1.0
							elif obj[0]>52.92107137034671:
								# {"feature": "workclass", "instances": 16, "metric_value": 0.0368, "depth": 8}
								if obj[1]<=5:
									# {"feature": "occupation", "instances": 15, "metric_value": 0.028, "depth": 9}
									if obj[4]>0:
										# {"feature": "hours-per-week", "instances": 14, "metric_value": 0.032, "depth": 10}
										if obj[10]>5:
											# {"feature": "gender", "instances": 13, "metric_value": 0.0129, "depth": 11}
											if obj[7]<=0:
												# {"feature": "native-country", "instances": 10, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.4
											elif obj[7]>0:
												return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[10]<=5:
											return 0
										else: return 0.0
									elif obj[4]<=0:
										return 0
									else: return 0.0
								elif obj[1]>5:
									return 1
								else: return 1.0
							else: return 0.4375
						elif obj[6]<=2:
							return 1
						else: return 1.0
					else: return 0.7383177570093458
				else: return 0.37269772481040087
			elif obj[8]>3553.565418227216:
				# {"feature": "hours-per-week", "instances": 1234, "metric_value": 0.0102, "depth": 4}
				if obj[10]<=46.59886547811993:
					# {"feature": "age", "instances": 660, "metric_value": 0.0038, "depth": 5}
					if obj[0]>35.483204206310276:
						# {"feature": "occupation", "instances": 560, "metric_value": 0.0031, "depth": 6}
						if obj[4]>0:
							# {"feature": "relationship", "instances": 525, "metric_value": 0.0018, "depth": 7}
							if obj[5]<=0:
								# {"feature": "native-country", "instances": 403, "metric_value": 0.0042, "depth": 8}
								if obj[11]>16:
									# {"feature": "race", "instances": 391, "metric_value": 0.0011, "depth": 9}
									if obj[6]>1:
										# {"feature": "workclass", "instances": 368, "metric_value": 0.0006, "depth": 10}
										if obj[1]<=3:
											# {"feature": "gender", "instances": 232, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 232, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9224137931034483
											else: return 0.9224137931034483
										elif obj[1]>3:
											# {"feature": "gender", "instances": 136, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 136, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9411764705882353
											else: return 0.9411764705882353
										else: return 0.9411764705882353
									elif obj[6]<=1:
										# {"feature": "workclass", "instances": 23, "metric_value": 0.0451, "depth": 10}
										if obj[1]<=5:
											# {"feature": "gender", "instances": 18, "metric_value": 0.0, "depth": 11}
											if obj[7]<=1:
												# {"feature": "capital-loss", "instances": 18, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.8333333333333334
											else: return 0.8333333333333334
										elif obj[1]>5:
											return 1
										else: return 1.0
									else: return 0.8695652173913043
								elif obj[11]<=16:
									return 1
								else: return 1.0
							elif obj[5]>0:
								# {"feature": "gender", "instances": 122, "metric_value": 0.0154, "depth": 8}
								if obj[7]<=0:
									# {"feature": "race", "instances": 85, "metric_value": 0.0292, "depth": 9}
									if obj[6]>3:
										# {"feature": "native-country", "instances": 68, "metric_value": 0.0121, "depth": 10}
										if obj[11]>8:
											# {"feature": "workclass", "instances": 66, "metric_value": 0.0104, "depth": 11}
											if obj[1]<=5:
												# {"feature": "capital-loss", "instances": 63, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9365079365079365
											elif obj[1]>5:
												return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[11]<=8:
											return 0.5
										else: return 0.5
									elif obj[6]<=3:
										return 1
									else: return 1.0
								elif obj[7]>0:
									# {"feature": "native-country", "instances": 37, "metric_value": 0.0072, "depth": 9}
									if obj[11]>25:
										# {"feature": "workclass", "instances": 36, "metric_value": 0.0075, "depth": 10}
										if obj[1]<=2:
											# {"feature": "race", "instances": 22, "metric_value": 0.0008, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 19, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7368421052631579
											elif obj[6]<=2:
												return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[1]>2:
											# {"feature": "race", "instances": 14, "metric_value": 0.0305, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 12, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.8333333333333334
											elif obj[6]<=2:
												return 1
											else: return 1.0
										else: return 0.8571428571428571
									elif obj[11]<=25:
										return 1
									else: return 1.0
								else: return 0.7837837837837838
							else: return 0.8852459016393442
						elif obj[4]<=0:
							# {"feature": "relationship", "instances": 35, "metric_value": 0.0454, "depth": 7}
							if obj[5]<=4:
								# {"feature": "native-country", "instances": 29, "metric_value": 0.0199, "depth": 8}
								if obj[11]>29:
									# {"feature": "race", "instances": 27, "metric_value": 0.0325, "depth": 9}
									if obj[6]>1:
										# {"feature": "workclass", "instances": 26, "metric_value": 0.0358, "depth": 10}
										if obj[1]>2:
											# {"feature": "gender", "instances": 14, "metric_value": 0.0037, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 12, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.6666666666666666
											elif obj[7]<=0:
												return 0.5
											else: return 0.5
										elif obj[1]<=2:
											# {"feature": "gender", "instances": 12, "metric_value": 0.1585, "depth": 11}
											if obj[7]>0:
												return 1
											elif obj[7]<=0:
												return 0.6666666666666666
											else: return 0.6666666666666666
										else: return 0.9166666666666666
									elif obj[6]<=1:
										return 0
									else: return 0.0
								elif obj[11]<=29:
									return 1
								else: return 1.0
							elif obj[5]>4:
								return 1
							else: return 1.0
						else: return 0.8
					elif obj[0]<=35.483204206310276:
						# {"feature": "race", "instances": 100, "metric_value": 0.0217, "depth": 6}
						if obj[6]>2:
							# {"feature": "workclass", "instances": 91, "metric_value": 0.0196, "depth": 7}
							if obj[1]<=5:
								# {"feature": "occupation", "instances": 84, "metric_value": 0.0063, "depth": 8}
								if obj[4]>5:
									# {"feature": "native-country", "instances": 66, "metric_value": 0.0028, "depth": 9}
									if obj[11]>10:
										# {"feature": "relationship", "instances": 61, "metric_value": 0.0016, "depth": 10}
										if obj[5]<=3:
											# {"feature": "gender", "instances": 43, "metric_value": 0.006, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 42, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7857142857142857
											elif obj[7]<=0:
												return 1
											else: return 1.0
										elif obj[5]>3:
											# {"feature": "gender", "instances": 18, "metric_value": 0.0, "depth": 11}
											if obj[7]<=0:
												# {"feature": "capital-loss", "instances": 18, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7222222222222222
											else: return 0.7222222222222222
										else: return 0.7222222222222222
									elif obj[11]<=10:
										# {"feature": "relationship", "instances": 5, "metric_value": 0.0071, "depth": 10}
										if obj[5]>0:
											return 0.6666666666666666
										elif obj[5]<=0:
											return 0.5
										else: return 0.5
									else: return 0.6
								elif obj[4]<=5:
									# {"feature": "relationship", "instances": 18, "metric_value": 0.031, "depth": 9}
									if obj[5]<=1:
										# {"feature": "gender", "instances": 15, "metric_value": 0.0, "depth": 10}
										if obj[7]<=1:
											# {"feature": "capital-loss", "instances": 15, "metric_value": 0.0, "depth": 11}
											if obj[9]<=0:
												# {"feature": "native-country", "instances": 15, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 1
												else: return 0.8666666666666667
											else: return 0.8666666666666667
										else: return 0.8666666666666667
									elif obj[5]>1:
										return 1
									else: return 1.0
								else: return 0.8888888888888888
							elif obj[1]>5:
								return 1
							else: return 1.0
						elif obj[6]<=2:
							return 1
						else: return 1.0
					else: return 0.82
				elif obj[10]>46.59886547811993:
					# {"feature": "native-country", "instances": 574, "metric_value": 0.0062, "depth": 5}
					if obj[11]>36:
						# {"feature": "gender", "instances": 536, "metric_value": 0.0039, "depth": 6}
						if obj[7]>0:
							# {"feature": "age", "instances": 495, "metric_value": 0.0043, "depth": 7}
							if obj[0]<=45.78181818181818:
								# {"feature": "workclass", "instances": 260, "metric_value": 0.009, "depth": 8}
								if obj[1]<=4:
									# {"feature": "occupation", "instances": 210, "metric_value": 0.0154, "depth": 9}
									if obj[4]>7:
										# {"feature": "relationship", "instances": 117, "metric_value": 0.0036, "depth": 10}
										if obj[5]<=0:
											# {"feature": "race", "instances": 108, "metric_value": 0.0023, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 103, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9902912621359223
											elif obj[6]<=2:
												return 1
											else: return 1.0
										elif obj[5]>0:
											return 1
										else: return 1.0
									elif obj[4]<=7:
										# {"feature": "relationship", "instances": 93, "metric_value": 0.0056, "depth": 10}
										if obj[5]<=0:
											# {"feature": "race", "instances": 87, "metric_value": 0.0038, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 84, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9523809523809523
											elif obj[6]<=2:
												return 1
											else: return 1.0
										elif obj[5]>0:
											# {"feature": "race", "instances": 6, "metric_value": 0.0393, "depth": 11}
											if obj[6]>1:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.8
											elif obj[6]<=1:
												return 1
											else: return 1.0
										else: return 0.8333333333333334
									else: return 0.946236559139785
								elif obj[1]>4:
									# {"feature": "occupation", "instances": 50, "metric_value": 0.0187, "depth": 9}
									if obj[4]<=5:
										# {"feature": "relationship", "instances": 25, "metric_value": 0.0041, "depth": 10}
										if obj[5]<=0:
											# {"feature": "race", "instances": 24, "metric_value": 0.0, "depth": 11}
											if obj[6]<=4:
												# {"feature": "capital-loss", "instances": 24, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9583333333333334
											else: return 0.9583333333333334
										elif obj[5]>0:
											return 1
										else: return 1.0
									elif obj[4]>5:
										# {"feature": "race", "instances": 25, "metric_value": 0.0491, "depth": 10}
										if obj[6]>2:
											# {"feature": "relationship", "instances": 24, "metric_value": 0.0255, "depth": 11}
											if obj[5]<=0:
												# {"feature": "capital-loss", "instances": 22, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9090909090909091
											elif obj[5]>0:
												return 0.5
											else: return 0.5
										elif obj[6]<=2:
											return 0
										else: return 0.0
									else: return 0.84
								else: return 0.9
							elif obj[0]>45.78181818181818:
								# {"feature": "relationship", "instances": 235, "metric_value": 0.0066, "depth": 8}
								if obj[5]<=0:
									# {"feature": "workclass", "instances": 212, "metric_value": 0.0065, "depth": 9}
									if obj[1]<=2:
										# {"feature": "occupation", "instances": 115, "metric_value": 0.0592, "depth": 10}
										if obj[4]<=10:
											return 1
										elif obj[4]>10:
											# {"feature": "race", "instances": 16, "metric_value": 0.0167, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 14, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9285714285714286
											elif obj[6]<=2:
												return 1
											else: return 1.0
										else: return 0.9375
									elif obj[1]>2:
										# {"feature": "occupation", "instances": 97, "metric_value": 0.0175, "depth": 10}
										if obj[4]<=9:
											# {"feature": "race", "instances": 79, "metric_value": 0.0025, "depth": 11}
											if obj[6]>3:
												# {"feature": "capital-loss", "instances": 77, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.961038961038961
											elif obj[6]<=3:
												return 1
											else: return 1.0
										elif obj[4]>9:
											return 1
										else: return 1.0
									else: return 0.9690721649484536
								elif obj[5]>0:
									return 1
								else: return 1.0
							else: return 0.9829787234042553
						elif obj[7]<=0:
							# {"feature": "relationship", "instances": 41, "metric_value": 0.0956, "depth": 7}
							if obj[5]<=4:
								# {"feature": "workclass", "instances": 21, "metric_value": 0.0526, "depth": 8}
								if obj[1]<=5:
									# {"feature": "age", "instances": 20, "metric_value": 0.0973, "depth": 9}
									if obj[0]>45:
										# {"feature": "occupation", "instances": 12, "metric_value": 0.0248, "depth": 10}
										if obj[4]>2:
											# {"feature": "race", "instances": 11, "metric_value": 0.0288, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 10, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7
											elif obj[6]<=2:
												return 1
											else: return 1.0
										elif obj[4]<=2:
											return 1
										else: return 1.0
									elif obj[0]<=45:
										return 1
									else: return 1.0
								elif obj[1]>5:
									return 0
								else: return 0.0
							elif obj[5]>4:
								return 1
							else: return 1.0
						else: return 0.9024390243902439
					elif obj[11]<=36:
						return 1
					else: return 1.0
				else: return 0.9668989547038328
			else: return 0.9294975688816856
		else: return 0.6454431960049938
	elif obj[3]>2:
		# {"feature": "capital-gain", "instances": 19793, "metric_value": 0.0268, "depth": 2}
		if obj[8]<=4627.353797326818:
			# {"feature": "educational-num", "instances": 19373, "metric_value": 0.0219, "depth": 3}
			if obj[2]<=12:
				# {"feature": "age", "instances": 15515, "metric_value": 0.0118, "depth": 4}
				if obj[0]<=31.025652594263615:
					# {"feature": "relationship", "instances": 10110, "metric_value": 0.0063, "depth": 5}
					if obj[5]>1:
						# {"feature": "hours-per-week", "instances": 7045, "metric_value": 0.0038, "depth": 6}
						if obj[10]>32.351312987934705:
							# {"feature": "workclass", "instances": 4008, "metric_value": 0.0058, "depth": 7}
							if obj[1]<=2:
								# {"feature": "gender", "instances": 3580, "metric_value": 0.003, "depth": 8}
								if obj[7]>0:
									# {"feature": "native-country", "instances": 2142, "metric_value": 0.0034, "depth": 9}
									if obj[11]>29.455836926810342:
										# {"feature": "race", "instances": 1909, "metric_value": 0.0037, "depth": 10}
										if obj[6]>1:
											# {"feature": "occupation", "instances": 1845, "metric_value": 0.0031, "depth": 11}
											if obj[4]<=11:
												# {"feature": "capital-loss", "instances": 1698, "metric_value": 0.0005, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											elif obj[4]>11:
												# {"feature": "capital-loss", "instances": 147, "metric_value": 0.0012, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											else: return 0.013605442176870748
										elif obj[6]<=1:
											# {"feature": "occupation", "instances": 64, "metric_value": 0.1007, "depth": 11}
											if obj[4]>2:
												return 0
											elif obj[4]<=2:
												# {"feature": "capital-loss", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.15384615384615385
											else: return 0.15384615384615385
										else: return 0.03125
									elif obj[11]<=29.455836926810342:
										return 0
									else: return 0.0
								elif obj[7]<=0:
									# {"feature": "native-country", "instances": 1438, "metric_value": 0.018, "depth": 9}
									if obj[11]>36.1884561891516:
										return 0
									elif obj[11]<=36.1884561891516:
										# {"feature": "occupation", "instances": 145, "metric_value": 0.0259, "depth": 10}
										if obj[4]<=6:
											return 0
										elif obj[4]>6:
											# {"feature": "race", "instances": 69, "metric_value": 0.016, "depth": 11}
											if obj[6]>3:
												# {"feature": "capital-loss", "instances": 52, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.019230769230769232
											elif obj[6]<=3:
												return 0
											else: return 0.0
										else: return 0.014492753623188406
									else: return 0.006896551724137931
								else: return 0.0006954102920723226
							elif obj[1]>2:
								# {"feature": "occupation", "instances": 428, "metric_value": 0.0165, "depth": 8}
								if obj[4]>1:
									# {"feature": "native-country", "instances": 332, "metric_value": 0.0107, "depth": 9}
									if obj[11]>18:
										# {"feature": "race", "instances": 323, "metric_value": 0.0025, "depth": 10}
										if obj[6]>1:
											# {"feature": "capital-loss", "instances": 306, "metric_value": 0.0019, "depth": 11}
											if obj[9]<=0:
												# {"feature": "gender", "instances": 297, "metric_value": 0.0011, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.024096385542168676
											elif obj[9]>0:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											# {"feature": "gender", "instances": 17, "metric_value": 0.0588, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 10, "metric_value": 0.0354, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											elif obj[7]<=0:
												return 0
											else: return 0.0
										else: return 0.058823529411764705
									elif obj[11]<=18:
										# {"feature": "race", "instances": 9, "metric_value": 0.1218, "depth": 10}
										if obj[6]>1:
											# {"feature": "gender", "instances": 8, "metric_value": 0.0245, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.14285714285714285
											elif obj[7]<=0:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 1
										else: return 1.0
									else: return 0.2222222222222222
								elif obj[4]<=1:
									return 0
								else: return 0.0
							else: return 0.018691588785046728
						elif obj[10]<=32.351312987934705:
							# {"feature": "gender", "instances": 3037, "metric_value": 0.0082, "depth": 7}
							if obj[7]<=0:
								return 0
							elif obj[7]>0:
								# {"feature": "occupation", "instances": 1403, "metric_value": 0.0081, "depth": 8}
								if obj[4]>6:
									# {"feature": "race", "instances": 866, "metric_value": 0.0043, "depth": 9}
									if obj[6]>3:
										# {"feature": "workclass", "instances": 719, "metric_value": 0.0023, "depth": 10}
										if obj[1]<=2:
											# {"feature": "native-country", "instances": 657, "metric_value": 0.0016, "depth": 11}
											if obj[11]>33:
												# {"feature": "capital-loss", "instances": 619, "metric_value": 0.0007, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											elif obj[11]<=33:
												return 0
											else: return 0.0
										elif obj[1]>2:
											return 0
										else: return 0.0
									elif obj[6]<=3:
										return 0
									else: return 0.0
								elif obj[4]<=6:
									return 0
								else: return 0.0
							else: return 0.0014255167498218105
						else: return 0.0006585446163977609
					elif obj[5]<=1:
						# {"feature": "hours-per-week", "instances": 3065, "metric_value": 0.0083, "depth": 6}
						if obj[10]<=49.733384735409665:
							# {"feature": "capital-loss", "instances": 2645, "metric_value": 0.0064, "depth": 7}
							if obj[9]<=360.6701650659435:
								# {"feature": "workclass", "instances": 2570, "metric_value": 0.0038, "depth": 8}
								if obj[1]<=2:
									# {"feature": "native-country", "instances": 2299, "metric_value": 0.0033, "depth": 9}
									if obj[11]>36.343627664201826:
										# {"feature": "occupation", "instances": 2084, "metric_value": 0.0026, "depth": 10}
										if obj[4]<=9:
											# {"feature": "race", "instances": 1648, "metric_value": 0.0021, "depth": 11}
											if obj[6]>1:
												# {"feature": "gender", "instances": 1608, "metric_value": 0.0006, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.004132231404958678
											elif obj[6]<=1:
												# {"feature": "gender", "instances": 40, "metric_value": 0.0561, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.058823529411764705
											else: return 0.025
										elif obj[4]>9:
											# {"feature": "gender", "instances": 436, "metric_value": 0.0275, "depth": 11}
											if obj[7]>0:
												# {"feature": "race", "instances": 242, "metric_value": 0.0087, "depth": 12}
												if obj[6]>3:
													return 0
												elif obj[6]<=3:
													return 0
												else: return 0.0
											elif obj[7]<=0:
												return 0
											else: return 0.0
										else: return 0.011467889908256881
									elif obj[11]<=36.343627664201826:
										return 0
									else: return 0.0
								elif obj[1]>2:
									# {"feature": "occupation", "instances": 271, "metric_value": 0.0174, "depth": 9}
									if obj[4]>1:
										# {"feature": "race", "instances": 212, "metric_value": 0.0151, "depth": 10}
										if obj[6]>1:
											# {"feature": "native-country", "instances": 203, "metric_value": 0.0043, "depth": 11}
											if obj[11]>30:
												# {"feature": "gender", "instances": 191, "metric_value": 0.0034, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.03571428571428571
											elif obj[11]<=30:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											# {"feature": "gender", "instances": 9, "metric_value": 0.0644, "depth": 11}
											if obj[7]>0:
												# {"feature": "native-country", "instances": 7, "metric_value": 0.0477, "depth": 12}
												if obj[11]>36:
													return 0
												elif obj[11]<=36:
													return 0
												else: return 0.0
											elif obj[7]<=0:
												return 0
											else: return 0.0
										else: return 0.2222222222222222
									elif obj[4]<=1:
										return 0
									else: return 0.0
								else: return 0.02214022140221402
							elif obj[9]>360.6701650659435:
								# {"feature": "occupation", "instances": 75, "metric_value": 0.0269, "depth": 8}
								if obj[4]<=10:
									# {"feature": "native-country", "instances": 62, "metric_value": 0.0135, "depth": 9}
									if obj[11]>27:
										# {"feature": "gender", "instances": 57, "metric_value": 0.0133, "depth": 10}
										if obj[7]>0:
											# {"feature": "race", "instances": 34, "metric_value": 0.0069, "depth": 11}
											if obj[6]>2:
												# {"feature": "workclass", "instances": 31, "metric_value": 0.0181, "depth": 12}
												if obj[1]<=3:
													return 0
												elif obj[1]>3:
													return 0
												else: return 0.5
											elif obj[6]<=2:
												return 0.3333333333333333
											else: return 0.3333333333333333
										elif obj[7]<=0:
											# {"feature": "workclass", "instances": 23, "metric_value": 0.0247, "depth": 11}
											if obj[1]<=2:
												# {"feature": "race", "instances": 18, "metric_value": 0.0068, "depth": 12}
												if obj[6]>2:
													return 0
												elif obj[6]<=2:
													return 0
												else: return 0.0
											elif obj[1]>2:
												return 0
											else: return 0.0
										else: return 0.043478260869565216
									elif obj[11]<=27:
										return 0
									else: return 0.0
								elif obj[4]>10:
									return 0
								else: return 0.0
							else: return 0.08
						elif obj[10]>49.733384735409665:
							# {"feature": "workclass", "instances": 420, "metric_value": 0.0176, "depth": 7}
							if obj[1]<=2:
								# {"feature": "occupation", "instances": 356, "metric_value": 0.0104, "depth": 8}
								if obj[4]<=11:
									# {"feature": "race", "instances": 314, "metric_value": 0.0092, "depth": 9}
									if obj[6]>3:
										# {"feature": "native-country", "instances": 283, "metric_value": 0.0095, "depth": 10}
										if obj[11]>1:
											# {"feature": "gender", "instances": 282, "metric_value": 0.0057, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 195, "metric_value": 0.0021, "depth": 12}
												if obj[9]<=0:
													return 0
												elif obj[9]>0:
													return 0
												else: return 0.0
											elif obj[7]<=0:
												# {"feature": "capital-loss", "instances": 87, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.011494252873563218
											else: return 0.011494252873563218
										elif obj[11]<=1:
											return 1
										else: return 1.0
									elif obj[6]<=3:
										return 0
									else: return 0.0
								elif obj[4]>11:
									return 0
								else: return 0.0
							elif obj[1]>2:
								# {"feature": "occupation", "instances": 64, "metric_value": 0.028, "depth": 8}
								if obj[4]>1:
									# {"feature": "race", "instances": 56, "metric_value": 0.017, "depth": 9}
									if obj[6]>2:
										# {"feature": "capital-loss", "instances": 52, "metric_value": 0.0192, "depth": 10}
										if obj[9]<=1564:
											# {"feature": "gender", "instances": 48, "metric_value": 0.007, "depth": 11}
											if obj[7]>0:
												# {"feature": "native-country", "instances": 38, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.23684210526315788
											elif obj[7]<=0:
												# {"feature": "native-country", "instances": 10, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.1
											else: return 0.1
										elif obj[9]>1564:
											return 0
										else: return 0.0
									elif obj[6]<=2:
										return 0
									else: return 0.0
								elif obj[4]<=1:
									return 0
								else: return 0.0
							else: return 0.15625
						else: return 0.047619047619047616
					else: return 0.014029363784665579
				elif obj[0]>31.025652594263615:
					# {"feature": "race", "instances": 5405, "metric_value": 0.0052, "depth": 5}
					if obj[6]>3:
						# {"feature": "capital-loss", "instances": 4026, "metric_value": 0.0056, "depth": 6}
						if obj[9]<=433.3145654306578:
							# {"feature": "relationship", "instances": 3884, "metric_value": 0.0051, "depth": 7}
							if obj[5]<=1:
								# {"feature": "hours-per-week", "instances": 2263, "metric_value": 0.0047, "depth": 8}
								if obj[10]>38.259832081308:
									# {"feature": "workclass", "instances": 1546, "metric_value": 0.0035, "depth": 9}
									if obj[1]<=5:
										# {"feature": "occupation", "instances": 1456, "metric_value": 0.0021, "depth": 10}
										if obj[4]<=8:
											# {"feature": "native-country", "instances": 1061, "metric_value": 0.0007, "depth": 11}
											if obj[11]>15.108232912051406:
												# {"feature": "gender", "instances": 1012, "metric_value": 0.0001, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.046620046620046623
											elif obj[11]<=15.108232912051406:
												# {"feature": "gender", "instances": 49, "metric_value": 0.0334, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.0
											else: return 0.02040816326530612
										elif obj[4]>8:
											# {"feature": "gender", "instances": 395, "metric_value": 0.0028, "depth": 11}
											if obj[7]>0:
												# {"feature": "native-country", "instances": 252, "metric_value": 0.0017, "depth": 12}
												if obj[11]>10:
													return 0
												elif obj[11]<=10:
													return 0
												else: return 0.3333333333333333
											elif obj[7]<=0:
												# {"feature": "native-country", "instances": 143, "metric_value": 0.0052, "depth": 12}
												if obj[11]>30:
													return 0
												elif obj[11]<=30:
													return 0
												else: return 0.0
											else: return 0.055944055944055944
										else: return 0.08354430379746836
									elif obj[1]>5:
										# {"feature": "gender", "instances": 90, "metric_value": 0.0163, "depth": 10}
										if obj[7]>0:
											# {"feature": "occupation", "instances": 59, "metric_value": 0.0184, "depth": 11}
											if obj[4]<=11:
												# {"feature": "native-country", "instances": 55, "metric_value": 0.0155, "depth": 12}
												if obj[11]>25:
													return 0
												elif obj[11]<=25:
													return 0
												else: return 0.0
											elif obj[4]>11:
												return 0
											else: return 0.0
										elif obj[7]<=0:
											# {"feature": "occupation", "instances": 31, "metric_value": 0.1339, "depth": 11}
											if obj[4]<=7:
												return 0
											elif obj[4]>7:
												# {"feature": "native-country", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.25
											else: return 0.25
										else: return 0.06451612903225806
									else: return 0.16666666666666666
								elif obj[10]<=38.259832081308:
									# {"feature": "occupation", "instances": 717, "metric_value": 0.0068, "depth": 9}
									if obj[4]<=8:
										# {"feature": "workclass", "instances": 443, "metric_value": 0.0093, "depth": 10}
										if obj[1]<=2:
											# {"feature": "native-country", "instances": 319, "metric_value": 0.0044, "depth": 11}
											if obj[11]>32:
												# {"feature": "gender", "instances": 285, "metric_value": 0.0014, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.010869565217391304
											elif obj[11]<=32:
												return 0
											else: return 0.0
										elif obj[1]>2:
											# {"feature": "native-country", "instances": 124, "metric_value": 0.0162, "depth": 11}
											if obj[11]>21:
												# {"feature": "gender", "instances": 122, "metric_value": 0.0087, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.047619047619047616
											elif obj[11]<=21:
												return 0.5
											else: return 0.5
										else: return 0.03225806451612903
									elif obj[4]>8:
										# {"feature": "workclass", "instances": 274, "metric_value": 0.0029, "depth": 10}
										if obj[1]<=6:
											# {"feature": "native-country", "instances": 269, "metric_value": 0.0023, "depth": 11}
											if obj[11]>20:
												# {"feature": "gender", "instances": 262, "metric_value": 0.0008, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.04819277108433735
											elif obj[11]<=20:
												# {"feature": "gender", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[7]<=0:
													return 0
												else: return 0.14285714285714285
											else: return 0.14285714285714285
										elif obj[1]>6:
											# {"feature": "gender", "instances": 5, "metric_value": 0.0536, "depth": 11}
											if obj[7]<=0:
												return 0.25
											elif obj[7]>0:
												return 0
											else: return 0.0
										else: return 0.2
									else: return 0.043795620437956206
								else: return 0.02510460251046025
							elif obj[5]>1:
								# {"feature": "hours-per-week", "instances": 1621, "metric_value": 0.0108, "depth": 8}
								if obj[10]>26.535585196905977:
									# {"feature": "gender", "instances": 1384, "metric_value": 0.0038, "depth": 9}
									if obj[7]<=0:
										# {"feature": "native-country", "instances": 820, "metric_value": 0.0033, "depth": 10}
										if obj[11]>10:
											# {"feature": "occupation", "instances": 776, "metric_value": 0.0032, "depth": 11}
											if obj[4]<=11:
												# {"feature": "workclass", "instances": 737, "metric_value": 0.0016, "depth": 12}
												if obj[1]<=2:
													return 0
												elif obj[1]>2:
													return 0
												else: return 0.027586206896551724
											elif obj[4]>11:
												return 0
											else: return 0.0
										elif obj[11]<=10:
											return 0
										else: return 0.0
									elif obj[7]>0:
										# {"feature": "workclass", "instances": 564, "metric_value": 0.0116, "depth": 10}
										if obj[1]<=3:
											# {"feature": "native-country", "instances": 498, "metric_value": 0.0119, "depth": 11}
											if obj[11]>32:
												# {"feature": "occupation", "instances": 442, "metric_value": 0.0038, "depth": 12}
												if obj[4]>3:
													return 0
												elif obj[4]<=3:
													return 0
												else: return 0.06486486486486487
											elif obj[11]<=32:
												return 0
											else: return 0.0
										elif obj[1]>3:
											return 0
										else: return 0.0
									else: return 0.03546099290780142
								elif obj[10]<=26.535585196905977:
									return 0
								else: return 0.0
							else: return 0.01974090067859346
						elif obj[9]>433.3145654306578:
							# {"feature": "hours-per-week", "instances": 142, "metric_value": 0.0226, "depth": 7}
							if obj[10]<=41.26056338028169:
								# {"feature": "occupation", "instances": 98, "metric_value": 0.0237, "depth": 8}
								if obj[4]<=10:
									# {"feature": "workclass", "instances": 86, "metric_value": 0.0148, "depth": 9}
									if obj[1]<=6:
										# {"feature": "native-country", "instances": 85, "metric_value": 0.0139, "depth": 10}
										if obj[11]>32:
											# {"feature": "relationship", "instances": 79, "metric_value": 0.013, "depth": 11}
											if obj[5]<=3:
												# {"feature": "gender", "instances": 66, "metric_value": 0.007, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.06451612903225806
											elif obj[5]>3:
												# {"feature": "gender", "instances": 13, "metric_value": 0.0066, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.4
											else: return 0.3076923076923077
										elif obj[11]<=32:
											return 0
										else: return 0.0
									elif obj[1]>6:
										return 1
									else: return 1.0
								elif obj[4]>10:
									return 0
								else: return 0.0
							elif obj[10]>41.26056338028169:
								# {"feature": "occupation", "instances": 44, "metric_value": 0.0357, "depth": 8}
								if obj[4]>0:
									# {"feature": "workclass", "instances": 40, "metric_value": 0.0215, "depth": 9}
									if obj[1]<=2:
										# {"feature": "native-country", "instances": 29, "metric_value": 0.0182, "depth": 10}
										if obj[11]>1:
											# {"feature": "gender", "instances": 28, "metric_value": 0.0049, "depth": 11}
											if obj[7]>0:
												# {"feature": "relationship", "instances": 22, "metric_value": 0.0045, "depth": 12}
												if obj[5]<=3:
													return 0
												elif obj[5]>3:
													return 1
												else: return 0.6666666666666666
											elif obj[7]<=0:
												# {"feature": "relationship", "instances": 6, "metric_value": 0.0632, "depth": 12}
												if obj[5]<=1:
													return 0
												elif obj[5]>1:
													return 0
												else: return 0.0
											else: return 0.3333333333333333
										elif obj[11]<=1:
											return 1
										else: return 1.0
									elif obj[1]>2:
										# {"feature": "relationship", "instances": 11, "metric_value": 0.113, "depth": 10}
										if obj[5]<=3:
											# {"feature": "gender", "instances": 10, "metric_value": 0.0354, "depth": 11}
											if obj[7]>0:
												# {"feature": "native-country", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.125
											elif obj[7]<=0:
												return 0
											else: return 0.0
										elif obj[5]>3:
											return 1
										else: return 1.0
									else: return 0.18181818181818182
								elif obj[4]<=0:
									return 0
								else: return 0.0
							else: return 0.36363636363636365
						else: return 0.19718309859154928
					elif obj[6]<=3:
						# {"feature": "occupation", "instances": 1379, "metric_value": 0.0116, "depth": 6}
						if obj[4]<=8:
							# {"feature": "hours-per-week", "instances": 1014, "metric_value": 0.0096, "depth": 7}
							if obj[10]>38.76232741617357:
								# {"feature": "workclass", "instances": 756, "metric_value": 0.0087, "depth": 8}
								if obj[1]<=3:
									# {"feature": "native-country", "instances": 603, "metric_value": 0.0097, "depth": 9}
									if obj[11]>21.271970465558955:
										# {"feature": "capital-loss", "instances": 573, "metric_value": 0.0132, "depth": 10}
										if obj[9]<=2339:
											# {"feature": "relationship", "instances": 572, "metric_value": 0.0224, "depth": 11}
											if obj[5]<=3:
												return 0
											elif obj[5]>3:
												# {"feature": "gender", "instances": 222, "metric_value": 0.0074, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 0
												else: return 0.0
											else: return 0.009009009009009009
										elif obj[9]>2339:
											return 1
										else: return 1.0
									elif obj[11]<=21.271970465558955:
										# {"feature": "relationship", "instances": 30, "metric_value": 0.0061, "depth": 10}
										if obj[5]<=3:
											# {"feature": "gender", "instances": 21, "metric_value": 0.0348, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 15, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.06666666666666667
											elif obj[7]<=0:
												return 0
											else: return 0.0
										elif obj[5]>3:
											# {"feature": "gender", "instances": 9, "metric_value": 0.0421, "depth": 11}
											if obj[7]<=0:
												# {"feature": "capital-loss", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.14285714285714285
											elif obj[7]>0:
												return 0
											else: return 0.0
										else: return 0.1111111111111111
									else: return 0.06666666666666667
								elif obj[1]>3:
									return 0
								else: return 0.0
							elif obj[10]<=38.76232741617357:
								return 0
							else: return 0.0
						elif obj[4]>8:
							# {"feature": "hours-per-week", "instances": 365, "metric_value": 0.012, "depth": 7}
							if obj[10]>26.729880975034224:
								# {"feature": "workclass", "instances": 319, "metric_value": 0.0105, "depth": 8}
								if obj[1]<=5:
									# {"feature": "native-country", "instances": 305, "metric_value": 0.0074, "depth": 9}
									if obj[11]>23:
										# {"feature": "capital-loss", "instances": 292, "metric_value": 0.0027, "depth": 10}
										if obj[9]<=0:
											# {"feature": "gender", "instances": 282, "metric_value": 0.0014, "depth": 11}
											if obj[7]<=0:
												# {"feature": "relationship", "instances": 166, "metric_value": 0.059, "depth": 12}
												if obj[5]>3:
													return 0
												elif obj[5]<=3:
													return 0
												else: return 0.06756756756756757
											elif obj[7]>0:
												# {"feature": "relationship", "instances": 116, "metric_value": 0.0846, "depth": 12}
												if obj[5]<=3:
													return 0
												elif obj[5]>3:
													return 0
												else: return 0.125
											else: return 0.017241379310344827
										elif obj[9]>0:
											return 0
										else: return 0.0
									elif obj[11]<=23:
										# {"feature": "relationship", "instances": 13, "metric_value": 0.1175, "depth": 10}
										if obj[5]<=1:
											# {"feature": "gender", "instances": 7, "metric_value": 0.0232, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.2
											elif obj[7]<=0:
												return 0.5
											else: return 0.5
										elif obj[5]>1:
											return 0
										else: return 0.0
									else: return 0.15384615384615385
								elif obj[1]>5:
									# {"feature": "relationship", "instances": 14, "metric_value": 0.0604, "depth": 9}
									if obj[5]<=2:
										# {"feature": "native-country", "instances": 11, "metric_value": 0.0288, "depth": 10}
										if obj[11]>10:
											# {"feature": "gender", "instances": 10, "metric_value": 0.0133, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.2
											elif obj[7]<=0:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.4
											else: return 0.4
										elif obj[11]<=10:
											return 0
										else: return 0.0
									elif obj[5]>2:
										return 0
									else: return 0.0
								else: return 0.21428571428571427
							elif obj[10]<=26.729880975034224:
								return 0
							else: return 0.0
						else: return 0.03287671232876712
					else: return 0.012327773749093546
				else: return 0.036077705827937095
			elif obj[2]>12:
				# {"feature": "age", "instances": 3858, "metric_value": 0.0212, "depth": 4}
				if obj[0]<=34.047952306894764:
					# {"feature": "hours-per-week", "instances": 2457, "metric_value": 0.0197, "depth": 5}
					if obj[10]<=40.17134717134717:
						# {"feature": "capital-loss", "instances": 1732, "metric_value": 0.006, "depth": 6}
						if obj[9]<=0:
							# {"feature": "gender", "instances": 1673, "metric_value": 0.0038, "depth": 7}
							if obj[7]<=0:
								# {"feature": "relationship", "instances": 902, "metric_value": 0.0031, "depth": 8}
								if obj[5]<=3:
									# {"feature": "workclass", "instances": 856, "metric_value": 0.0029, "depth": 9}
									if obj[1]<=2:
										# {"feature": "occupation", "instances": 661, "metric_value": 0.0045, "depth": 10}
										if obj[4]>8:
											# {"feature": "native-country", "instances": 335, "metric_value": 0.0043, "depth": 11}
											if obj[11]>25:
												# {"feature": "race", "instances": 318, "metric_value": 0.0009, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 0
												else: return 0.05555555555555555
											elif obj[11]<=25:
												return 0
											else: return 0.0
										elif obj[4]<=8:
											# {"feature": "race", "instances": 326, "metric_value": 0.0082, "depth": 11}
											if obj[6]>2:
												# {"feature": "native-country", "instances": 273, "metric_value": 0.0023, "depth": 12}
												if obj[11]>31:
													return 0
												elif obj[11]<=31:
													return 0
												else: return 0.0
											elif obj[6]<=2:
												return 0
											else: return 0.0
										else: return 0.009202453987730062
									elif obj[1]>2:
										# {"feature": "race", "instances": 195, "metric_value": 0.056, "depth": 10}
										if obj[6]>1:
											return 0
										elif obj[6]<=1:
											# {"feature": "occupation", "instances": 10, "metric_value": 0.2, "depth": 11}
											if obj[4]>0:
												return 0
											elif obj[4]<=0:
												return 0.5
											else: return 0.5
										else: return 0.1
									else: return 0.005128205128205128
								elif obj[5]>3:
									return 0
								else: return 0.0
							elif obj[7]>0:
								# {"feature": "relationship", "instances": 771, "metric_value": 0.0065, "depth": 8}
								if obj[5]<=1:
									# {"feature": "occupation", "instances": 448, "metric_value": 0.006, "depth": 9}
									if obj[4]>7:
										# {"feature": "workclass", "instances": 277, "metric_value": 0.0069, "depth": 10}
										if obj[1]<=6:
											# {"feature": "native-country", "instances": 276, "metric_value": 0.0023, "depth": 11}
											if obj[11]>2:
												# {"feature": "race", "instances": 271, "metric_value": 0.0012, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 0
												else: return 0.03333333333333333
											elif obj[11]<=2:
												return 0
											else: return 0.0
										elif obj[1]>6:
											return 1
										else: return 1.0
									elif obj[4]<=7:
										# {"feature": "workclass", "instances": 171, "metric_value": 0.0118, "depth": 10}
										if obj[1]<=2:
											# {"feature": "race", "instances": 146, "metric_value": 0.0101, "depth": 11}
											if obj[6]>3:
												# {"feature": "native-country", "instances": 129, "metric_value": 0.0049, "depth": 12}
												if obj[11]>32:
													return 0
												elif obj[11]<=32:
													return 0
												else: return 0.0
											elif obj[6]<=3:
												return 0
											else: return 0.0
										elif obj[1]>2:
											return 0
										else: return 0.0
									else: return 0.023391812865497075
								elif obj[5]>1:
									# {"feature": "workclass", "instances": 323, "metric_value": 0.014, "depth": 9}
									if obj[1]<=2:
										# {"feature": "race", "instances": 255, "metric_value": 0.0119, "depth": 10}
										if obj[6]>3:
											# {"feature": "occupation", "instances": 214, "metric_value": 0.0109, "depth": 11}
											if obj[4]>0:
												# {"feature": "native-country", "instances": 185, "metric_value": 0.0009, "depth": 12}
												if obj[11]>25:
													return 0
												elif obj[11]<=25:
													return 0
												else: return 0.0
											elif obj[4]<=0:
												return 0
											else: return 0.0
										elif obj[6]<=3:
											return 0
										else: return 0.0
									elif obj[1]>2:
										return 0
									else: return 0.0
								else: return 0.015479876160990712
							else: return 0.03501945525291829
						elif obj[9]>0:
							# {"feature": "occupation", "instances": 59, "metric_value": 0.015, "depth": 7}
							if obj[4]>0:
								# {"feature": "native-country", "instances": 55, "metric_value": 0.007, "depth": 8}
								if obj[11]>4:
									# {"feature": "workclass", "instances": 53, "metric_value": 0.0037, "depth": 9}
									if obj[1]<=5:
										# {"feature": "race", "instances": 52, "metric_value": 0.0027, "depth": 10}
										if obj[6]>1:
											# {"feature": "gender", "instances": 48, "metric_value": 0.0025, "depth": 11}
											if obj[7]<=0:
												# {"feature": "relationship", "instances": 27, "metric_value": 0.0072, "depth": 12}
												if obj[5]<=1:
													return 0
												elif obj[5]>1:
													return 0
												else: return 0.2222222222222222
											elif obj[7]>0:
												# {"feature": "relationship", "instances": 21, "metric_value": 0.0327, "depth": 12}
												if obj[5]<=1:
													return 0
												elif obj[5]>1:
													return 0
												else: return 0.0
											else: return 0.09523809523809523
										elif obj[6]<=1:
											return 0.25
										else: return 0.25
									elif obj[1]>5:
										return 0
									else: return 0.0
								elif obj[11]<=4:
									return 0
								else: return 0.0
							elif obj[4]<=0:
								return 0.5
							else: return 0.5
						else: return 0.15254237288135594
					elif obj[10]>40.17134717134717:
						# {"feature": "capital-loss", "instances": 725, "metric_value": 0.0052, "depth": 6}
						if obj[9]<=2339:
							# {"feature": "relationship", "instances": 722, "metric_value": 0.0053, "depth": 7}
							if obj[5]<=1:
								# {"feature": "occupation", "instances": 575, "metric_value": 0.0021, "depth": 8}
								if obj[4]>2:
									# {"feature": "workclass", "instances": 531, "metric_value": 0.0018, "depth": 9}
									if obj[1]<=3:
										# {"feature": "native-country", "instances": 414, "metric_value": 0.0011, "depth": 10}
										if obj[11]>2:
											# {"feature": "race", "instances": 412, "metric_value": 0.0006, "depth": 11}
											if obj[6]>0:
												# {"feature": "gender", "instances": 411, "metric_value": 0.0001, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.16666666666666666
											elif obj[6]<=0:
												return 0
											else: return 0.0
										elif obj[11]<=2:
											return 0
										else: return 0.0
									elif obj[1]>3:
										# {"feature": "race", "instances": 117, "metric_value": 0.0046, "depth": 10}
										if obj[6]>1:
											# {"feature": "native-country", "instances": 114, "metric_value": 0.0032, "depth": 11}
											if obj[11]>10:
												# {"feature": "gender", "instances": 112, "metric_value": 0.0007, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.12962962962962962
											elif obj[11]<=10:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 0
										else: return 0.0
									else: return 0.1111111111111111
								elif obj[4]<=2:
									# {"feature": "gender", "instances": 44, "metric_value": 0.076, "depth": 9}
									if obj[7]>0:
										# {"feature": "workclass", "instances": 23, "metric_value": 0.0263, "depth": 10}
										if obj[1]<=2:
											# {"feature": "race", "instances": 20, "metric_value": 0.0242, "depth": 11}
											if obj[6]>1:
												# {"feature": "native-country", "instances": 18, "metric_value": 0.01, "depth": 12}
												if obj[11]>8:
													return 0
												elif obj[11]<=8:
													return 0
												else: return 0.0
											elif obj[6]<=1:
												return 0.5
											else: return 0.5
										elif obj[1]>2:
											return 0
										else: return 0.0
									elif obj[7]<=0:
										return 0
									else: return 0.0
								else: return 0.06818181818181818
							elif obj[5]>1:
								# {"feature": "workclass", "instances": 147, "metric_value": 0.0238, "depth": 8}
								if obj[1]<=3:
									# {"feature": "occupation", "instances": 121, "metric_value": 0.0148, "depth": 9}
									if obj[4]<=9:
										# {"feature": "native-country", "instances": 76, "metric_value": 0.0118, "depth": 10}
										if obj[11]>29:
											# {"feature": "race", "instances": 70, "metric_value": 0.0252, "depth": 11}
											if obj[6]>2:
												# {"feature": "gender", "instances": 59, "metric_value": 0.0011, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.12
											elif obj[6]<=2:
												return 0
											else: return 0.0
										elif obj[11]<=29:
											# {"feature": "gender", "instances": 6, "metric_value": 0.0632, "depth": 11}
											if obj[7]>0:
												# {"feature": "race", "instances": 5, "metric_value": 0.0071, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 0
												else: return 0.5
											elif obj[7]<=0:
												return 0
											else: return 0.0
										else: return 0.3333333333333333
									elif obj[4]>9:
										# {"feature": "gender", "instances": 45, "metric_value": 0.0257, "depth": 10}
										if obj[7]>0:
											# {"feature": "race", "instances": 31, "metric_value": 0.022, "depth": 11}
											if obj[6]>2:
												# {"feature": "native-country", "instances": 24, "metric_value": 0.0044, "depth": 12}
												if obj[11]>26:
													return 0
												elif obj[11]<=26:
													return 0
												else: return 0.0
											elif obj[6]<=2:
												return 0
											else: return 0.0
										elif obj[7]<=0:
											return 0
										else: return 0.0
									else: return 0.022222222222222223
								elif obj[1]>3:
									return 0
								else: return 0.0
							else: return 0.061224489795918366
						elif obj[9]>2339:
							return 1
						else: return 1.0
					else: return 0.13655172413793104
				elif obj[0]>34.047952306894764:
					# {"feature": "hours-per-week", "instances": 1401, "metric_value": 0.0103, "depth": 5}
					if obj[10]<=41.82441113490364:
						# {"feature": "gender", "instances": 907, "metric_value": 0.0069, "depth": 6}
						if obj[7]<=0:
							# {"feature": "capital-loss", "instances": 520, "metric_value": 0.008, "depth": 7}
							if obj[9]<=2258:
								# {"feature": "native-country", "instances": 517, "metric_value": 0.0032, "depth": 8}
								if obj[11]>36.06963249516441:
									# {"feature": "workclass", "instances": 464, "metric_value": 0.0033, "depth": 9}
									if obj[1]<=6:
										# {"feature": "relationship", "instances": 455, "metric_value": 0.0029, "depth": 10}
										if obj[5]<=1:
											# {"feature": "occupation", "instances": 276, "metric_value": 0.0167, "depth": 11}
											if obj[4]<=9:
												# {"feature": "race", "instances": 252, "metric_value": 0.0024, "depth": 12}
												if obj[6]>1:
													return 0
												elif obj[6]<=1:
													return 0
												else: return 0.0
											elif obj[4]>9:
												return 0
											else: return 0.0
										elif obj[5]>1:
											# {"feature": "occupation", "instances": 179, "metric_value": 0.0229, "depth": 11}
											if obj[4]>2:
												# {"feature": "race", "instances": 151, "metric_value": 0.0031, "depth": 12}
												if obj[6]>0:
													return 0
												elif obj[6]<=0:
													return 0
												else: return 0.0
											elif obj[4]<=2:
												return 0
											else: return 0.0
										else: return 0.07262569832402235
									elif obj[1]>6:
										return 0
									else: return 0.0
								elif obj[11]<=36.06963249516441:
									# {"feature": "occupation", "instances": 53, "metric_value": 0.0461, "depth": 9}
									if obj[4]>0:
										# {"feature": "workclass", "instances": 44, "metric_value": 0.0202, "depth": 10}
										if obj[1]<=5:
											# {"feature": "race", "instances": 43, "metric_value": 0.0054, "depth": 11}
											if obj[6]<=2:
												# {"feature": "relationship", "instances": 25, "metric_value": 0.0022, "depth": 12}
												if obj[5]<=3:
													return 0
												elif obj[5]>3:
													return 0
												else: return 0.3333333333333333
											elif obj[6]>2:
												# {"feature": "relationship", "instances": 18, "metric_value": 0.1005, "depth": 12}
												if obj[5]<=1:
													return 0
												elif obj[5]>1:
													return 0
												else: return 0.0
											else: return 0.16666666666666666
										elif obj[1]>5:
											return 1
										else: return 1.0
									elif obj[4]<=0:
										return 0
									else: return 0.0
								else: return 0.20754716981132076
							elif obj[9]>2258:
								return 1
							else: return 1.0
						elif obj[7]>0:
							# {"feature": "capital-loss", "instances": 387, "metric_value": 0.0197, "depth": 7}
							if obj[9]<=2258:
								# {"feature": "native-country", "instances": 379, "metric_value": 0.0103, "depth": 8}
								if obj[11]>10:
									# {"feature": "relationship", "instances": 364, "metric_value": 0.0084, "depth": 9}
									if obj[5]<=1:
										# {"feature": "occupation", "instances": 297, "metric_value": 0.0071, "depth": 10}
										if obj[4]>8:
											# {"feature": "race", "instances": 168, "metric_value": 0.013, "depth": 11}
											if obj[6]>2:
												# {"feature": "workclass", "instances": 151, "metric_value": 0.0021, "depth": 12}
												if obj[1]<=4:
													return 0
												elif obj[1]>4:
													return 0
												else: return 0.24
											elif obj[6]<=2:
												# {"feature": "workclass", "instances": 17, "metric_value": 0.0689, "depth": 12}
												if obj[1]<=2:
													return 0
												elif obj[1]>2:
													return 0
												else: return 0.0
											else: return 0.058823529411764705
										elif obj[4]<=8:
											# {"feature": "workclass", "instances": 129, "metric_value": 0.0093, "depth": 11}
											if obj[1]<=5:
												# {"feature": "race", "instances": 112, "metric_value": 0.0037, "depth": 12}
												if obj[6]>0:
													return 0
												elif obj[6]<=0:
													return 0
												else: return 0.0
											elif obj[1]>5:
												# {"feature": "race", "instances": 17, "metric_value": 0.0001, "depth": 12}
												if obj[6]>2:
													return 0
												elif obj[6]<=2:
													return 0
												else: return 0.3333333333333333
											else: return 0.35294117647058826
										else: return 0.17054263565891473
									elif obj[5]>1:
										# {"feature": "race", "instances": 67, "metric_value": 0.0194, "depth": 10}
										if obj[6]>1:
											# {"feature": "occupation", "instances": 59, "metric_value": 0.0207, "depth": 11}
											if obj[4]<=11:
												# {"feature": "workclass", "instances": 52, "metric_value": 0.0158, "depth": 12}
												if obj[1]<=5:
													return 0
												elif obj[1]>5:
													return 0
												else: return 0.3333333333333333
											elif obj[4]>11:
												return 0
											else: return 0.0
										elif obj[6]<=1:
											return 0
										else: return 0.0
									else: return 0.08955223880597014
								elif obj[11]<=10:
									return 0
								else: return 0.0
							elif obj[9]>2258:
								return 1
							else: return 1.0
						else: return 0.2248062015503876
					elif obj[10]>41.82441113490364:
						# {"feature": "capital-loss", "instances": 494, "metric_value": 0.0162, "depth": 6}
						if obj[9]<=2258:
							# {"feature": "relationship", "instances": 483, "metric_value": 0.0044, "depth": 7}
							if obj[5]<=1:
								# {"feature": "occupation", "instances": 395, "metric_value": 0.0046, "depth": 8}
								if obj[4]<=12:
									# {"feature": "native-country", "instances": 390, "metric_value": 0.0012, "depth": 9}
									if obj[11]>37:
										# {"feature": "race", "instances": 364, "metric_value": 0.0018, "depth": 10}
										if obj[6]>3:
											# {"feature": "workclass", "instances": 333, "metric_value": 0.0017, "depth": 11}
											if obj[1]<=4:
												# {"feature": "gender", "instances": 274, "metric_value": 0.0025, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.26785714285714285
											elif obj[1]>4:
												# {"feature": "gender", "instances": 59, "metric_value": 0.0029, "depth": 12}
												if obj[7]>0:
													return 0
												elif obj[7]<=0:
													return 0
												else: return 0.48148148148148145
											else: return 0.423728813559322
										elif obj[6]<=3:
											# {"feature": "workclass", "instances": 31, "metric_value": 0.0159, "depth": 11}
											if obj[1]<=6:
												# {"feature": "gender", "instances": 30, "metric_value": 0.0011, "depth": 12}
												if obj[7]<=0:
													return 1
												elif obj[7]>0:
													return 0
												else: return 0.4666666666666667
											elif obj[1]>6:
												return 0
											else: return 0.0
										else: return 0.4838709677419355
									elif obj[11]<=37:
										# {"feature": "race", "instances": 26, "metric_value": 0.0688, "depth": 10}
										if obj[6]>2:
											# {"feature": "workclass", "instances": 20, "metric_value": 0.0399, "depth": 11}
											if obj[1]<=6:
												# {"feature": "gender", "instances": 19, "metric_value": 0.0634, "depth": 12}
												if obj[7]<=0:
													return 0
												elif obj[7]>0:
													return 1
												else: return 0.5
											elif obj[1]>6:
												return 1
											else: return 1.0
										elif obj[6]<=2:
											return 0
										else: return 0.0
									else: return 0.23076923076923078
								elif obj[4]>12:
									return 0
								else: return 0.0
							elif obj[5]>1:
								# {"feature": "race", "instances": 88, "metric_value": 0.02, "depth": 8}
								if obj[6]>1:
									# {"feature": "occupation", "instances": 81, "metric_value": 0.0196, "depth": 9}
									if obj[4]>2:
										# {"feature": "gender", "instances": 75, "metric_value": 0.0165, "depth": 10}
										if obj[7]<=0:
											# {"feature": "workclass", "instances": 38, "metric_value": 0.038, "depth": 11}
											if obj[1]<=4:
												# {"feature": "native-country", "instances": 31, "metric_value": 0.0144, "depth": 12}
												if obj[11]>26:
													return 0
												elif obj[11]<=26:
													return 0
												else: return 0.0
											elif obj[1]>4:
												return 0
											else: return 0.0
										elif obj[7]>0:
											# {"feature": "workclass", "instances": 37, "metric_value": 0.029, "depth": 11}
											if obj[1]<=2:
												# {"feature": "native-country", "instances": 21, "metric_value": 0.0, "depth": 12}
												if obj[11]<=38:
													return 0
												else: return 0.19047619047619047
											elif obj[1]>2:
												# {"feature": "native-country", "instances": 16, "metric_value": 0.0323, "depth": 12}
												if obj[11]>1:
													return 1
												elif obj[11]<=1:
													return 0
												else: return 0.0
											else: return 0.5
										else: return 0.32432432432432434
									elif obj[4]<=2:
										return 0
									else: return 0.0
								elif obj[6]<=1:
									return 0
								else: return 0.0
							else: return 0.19318181818181818
						elif obj[9]>2258:
							return 1
						else: return 1.0
					else: return 0.32793522267206476
				else: return 0.22127052105638828
			else: return 0.11871435977190253
		elif obj[8]>4627.353797326818:
			# {"feature": "native-country", "instances": 420, "metric_value": 0.0174, "depth": 3}
			if obj[11]>34:
				# {"feature": "educational-num", "instances": 397, "metric_value": 0.0144, "depth": 4}
				if obj[2]<=14:
					# {"feature": "workclass", "instances": 364, "metric_value": 0.0105, "depth": 5}
					if obj[1]<=6:
						# {"feature": "hours-per-week", "instances": 353, "metric_value": 0.0085, "depth": 6}
						if obj[10]<=43.946175637393765:
							# {"feature": "gender", "instances": 193, "metric_value": 0.0078, "depth": 7}
							if obj[7]>0:
								# {"feature": "age", "instances": 107, "metric_value": 0.0166, "depth": 8}
								if obj[0]<=67.09427150953212:
									# {"feature": "relationship", "instances": 102, "metric_value": 0.0054, "depth": 9}
									if obj[5]<=1:
										# {"feature": "race", "instances": 76, "metric_value": 0.0101, "depth": 10}
										if obj[6]>0:
											# {"feature": "occupation", "instances": 75, "metric_value": 0.0076, "depth": 11}
											if obj[4]<=12:
												# {"feature": "capital-loss", "instances": 70, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7285714285714285
											elif obj[4]>12:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.4
											else: return 0.4
										elif obj[6]<=0:
											return 0
										else: return 0.0
									elif obj[5]>1:
										# {"feature": "occupation", "instances": 26, "metric_value": 0.0245, "depth": 10}
										if obj[4]<=3:
											# {"feature": "race", "instances": 13, "metric_value": 0.0545, "depth": 11}
											if obj[6]>1:
												# {"feature": "capital-loss", "instances": 11, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.6363636363636364
											elif obj[6]<=1:
												return 1
											else: return 1.0
										elif obj[4]>3:
											# {"feature": "race", "instances": 13, "metric_value": 0.025, "depth": 11}
											if obj[6]>2:
												# {"feature": "capital-loss", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.5
											elif obj[6]<=2:
												# {"feature": "capital-loss", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 0
												else: return 0.2
											else: return 0.2
										else: return 0.38461538461538464
									else: return 0.5384615384615384
								elif obj[0]>67.09427150953212:
									return 1
								else: return 1.0
							elif obj[7]<=0:
								# {"feature": "relationship", "instances": 86, "metric_value": 0.0075, "depth": 8}
								if obj[5]<=3:
									# {"feature": "race", "instances": 68, "metric_value": 0.0095, "depth": 9}
									if obj[6]>3:
										# {"feature": "age", "instances": 62, "metric_value": 0.0084, "depth": 10}
										if obj[0]>17:
											# {"feature": "occupation", "instances": 61, "metric_value": 0.0079, "depth": 11}
											if obj[4]<=12:
												# {"feature": "capital-loss", "instances": 60, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.5166666666666667
											elif obj[4]>12:
												return 1
											else: return 1.0
										elif obj[0]<=17:
											return 0
										else: return 0.0
									elif obj[6]<=3:
										# {"feature": "occupation", "instances": 6, "metric_value": 0.3727, "depth": 10}
										if obj[4]<=10:
											return 1
										elif obj[4]>10:
											return 0
										else: return 0.0
									else: return 0.8333333333333334
								elif obj[5]>3:
									# {"feature": "race", "instances": 18, "metric_value": 0.0865, "depth": 9}
									if obj[6]>2:
										# {"feature": "age", "instances": 14, "metric_value": 0.1036, "depth": 10}
										if obj[0]>34:
											# {"feature": "occupation", "instances": 11, "metric_value": 0.0526, "depth": 11}
											if obj[4]<=9:
												# {"feature": "capital-loss", "instances": 10, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.6
											elif obj[4]>9:
												return 0
											else: return 0.0
										elif obj[0]<=34:
											return 0
										else: return 0.0
									elif obj[6]<=2:
										return 0
									else: return 0.0
								else: return 0.3333333333333333
							else: return 0.5
						elif obj[10]>43.946175637393765:
							# {"feature": "age", "instances": 160, "metric_value": 0.0172, "depth": 7}
							if obj[0]<=39.36875:
								# {"feature": "occupation", "instances": 89, "metric_value": 0.0033, "depth": 8}
								if obj[4]>0:
									# {"feature": "relationship", "instances": 81, "metric_value": 0.0006, "depth": 9}
									if obj[5]<=2:
										# {"feature": "race", "instances": 64, "metric_value": 0.0103, "depth": 10}
										if obj[6]>0:
											# {"feature": "gender", "instances": 62, "metric_value": 0.0011, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 42, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.7142857142857143
											elif obj[7]<=0:
												# {"feature": "capital-loss", "instances": 20, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.65
											else: return 0.65
										elif obj[6]<=0:
											return 1
										else: return 1.0
									elif obj[5]>2:
										# {"feature": "gender", "instances": 17, "metric_value": 0.0967, "depth": 10}
										if obj[7]>0:
											# {"feature": "race", "instances": 13, "metric_value": 0.0434, "depth": 11}
											if obj[6]>0:
												# {"feature": "capital-loss", "instances": 12, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.5833333333333334
											elif obj[6]<=0:
												return 0
											else: return 0.0
										elif obj[7]<=0:
											return 1
										else: return 1.0
									else: return 0.6470588235294118
								elif obj[4]<=0:
									# {"feature": "relationship", "instances": 8, "metric_value": 0.067, "depth": 9}
									if obj[5]<=1:
										# {"feature": "race", "instances": 7, "metric_value": 0.0663, "depth": 10}
										if obj[6]>1:
											# {"feature": "gender", "instances": 6, "metric_value": 0.0286, "depth": 11}
											if obj[7]<=0:
												return 0.3333333333333333
											elif obj[7]>0:
												return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[6]<=1:
											return 1
										else: return 1.0
									elif obj[5]>1:
										return 0
									else: return 0.0
								else: return 0.5
							elif obj[0]>39.36875:
								# {"feature": "occupation", "instances": 71, "metric_value": 0.0109, "depth": 8}
								if obj[4]<=11:
									# {"feature": "relationship", "instances": 67, "metric_value": 0.0115, "depth": 9}
									if obj[5]<=3:
										# {"feature": "race", "instances": 57, "metric_value": 0.0075, "depth": 10}
										if obj[6]>2:
											# {"feature": "gender", "instances": 54, "metric_value": 0.0043, "depth": 11}
											if obj[7]>0:
												# {"feature": "capital-loss", "instances": 30, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.9333333333333333
											elif obj[7]<=0:
												# {"feature": "capital-loss", "instances": 24, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.875
											else: return 0.875
										elif obj[6]<=2:
											return 0.6666666666666666
										else: return 0.6666666666666666
									elif obj[5]>3:
										# {"feature": "gender", "instances": 10, "metric_value": 0.034, "depth": 10}
										if obj[7]<=0:
											# {"feature": "race", "instances": 9, "metric_value": 0.0, "depth": 11}
											if obj[6]<=4:
												# {"feature": "capital-loss", "instances": 9, "metric_value": 0.0, "depth": 12}
												if obj[9]<=0:
													return 1
												else: return 0.6666666666666666
											else: return 0.6666666666666666
										elif obj[7]>0:
											return 1
										else: return 1.0
									else: return 0.7
								elif obj[4]>11:
									return 1
								else: return 1.0
							else: return 0.8732394366197183
						else: return 0.7625
					elif obj[1]>6:
						return 1
					else: return 1.0
				elif obj[2]>14:
					# {"feature": "race", "instances": 33, "metric_value": 0.1411, "depth": 5}
					if obj[6]>2:
						return 1
					elif obj[6]<=2:
						return 0.5
					else: return 0.5
				else: return 0.9696969696969697
			elif obj[11]<=34:
				return 1
			else: return 1.0
		else: return 0.7214285714285714
	else: return 0.051432324559187594

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total_mensal = sp + rj + mg + es + outros

percentual_sp = (67836.43/total_mensal) * 100
percentual_rj = (36678.66/total_mensal) * 100
percentual_mg = (29229.88/total_mensal) * 100
percentual_es = (27165.48/total_mensal) * 100
percentual_outros = (19849.53/total_mensal) * 100

print('O percentual de representação de cada estado:')
resultado = '{:.2f}'.format(percentual_sp),'{:.2f}'.format(percentual_rj),'{:.2f}'.format(percentual_mg),'{:.2f}'.format(percentual_es),'{:.2f}'.format(percentual_outros)
print(' SP: ',resultado[0],'%', '\n RJ: ', resultado[1],'%', '\n MG: ', resultado[2],'%', '\n ES: ', resultado[3],'%', '\n Outros: ',resultado[4],'%')



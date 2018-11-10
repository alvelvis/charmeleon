# charmeleon
**charmeleon** compara palavras usando como base um arquivo fonte.

# Como usar

	>> charmeleon.py fonte:codificação <parâmetros>

	fonte: arquivo com as palavras do domínio
	codificação: codificação do arquivo com as palavras do domínio (padrão: utf8)
	
	Parâmetros:
	-fonetizar: comparar os sons das palavras
	-spaces: número de espaços que serão cortados (padrão: infinito)
	-limit: porcentagem mínima a ser mostrada (padrão: 0)
	-x: pixels reservados para a palavra (padrão: 30)
	-y: pixels reservados para a porcentagem (padrão: 30)

* Para comparar os sons (parâmetro *-fonetizar*), é necessário ter, na mesma pasta do **charmeleon**, o [**fonetizador**](https://github.com/alvelvis/fonetizador).
* Para cortar espaços à direita do arquivo fonte (parâmetro *-spaces*), considere usar números negativos.
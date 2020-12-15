def encontra_familia_chave_C():
    c1 = input("A.Pétalas unidas às sépalas, formando com estas um unico tubo\nB.Pétalas livres das sépalas\nEscolha a opção:").upper()
    if c1 == "A":
        return "\n"+" "*3+"A Familia não pode ser encontrada na Chave C. Retorne e use a Chave B.\n"
    elif c1 == "B":
        c2 = input("A.Ovário súpero\nB.Ovario ínfero\nEscolha a opção:").upper()
        if c2 == "A":
            c3 = input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção:").upper()
            if c3 == "A":
                    c4 = input("A.Folhas opostas\nB.Folhas alternas\nEscolha a opção:").upper()
                    if c4 == "A":
                        return "Família Apocynaceae"
                    elif c4 == "B":
                        c5 = input("A.Gineceu unicarpelar\nB.Gineceu bi-pluricarpelar\nEscolha a opção:").upper()
                        if c5 == "A":
                            return "Família Fabaceae(Leguminosae)"
                        elif c5 == "B":
                            c6 = input("A.Ovario uni-bilocular\nB.Ovario tri-plurilocular\nEscolha a opção:").upper()
                            if c6 == "A":
                                c7 = input("A.Lóculos do ovário com um único óvulo\nB.Lóculos do ovário com dois ou mais óvulos\nEscolha a opção:").upper()
                                if c7 == "A":
                                    c8 = input("A.Cálice gamossépalo\nB.Cálice dialissépalo\nEscolha a opção:").upper()
                                    if c8 == "A":
                                        return "Família Plumbaginaceae"
                                    elif c8 == "B":
                                        c9 = input("A.Fruto carnoso \nB.Fruto seco\nEscolha a opção:").upper()
                                        if c9 == "A":
                                            return "Família Sapotaceae"
                                        elif c9 == "B":
                                            return "Família Euphorbiaceae"
                                elif c7 == "B":
                                    c10 = input("A.Lóculos do ovário biovulados\nB.Lóculos do ovário pluriovulados\nEscolha a opção:").upper()
                                    if c10 == "A":
                                        return "Família Vitaceae"
                                    elif c10 == "B":
                                        c11 = input("A.Prefloração do cálice imbricada\nB.Prefloração do cálice valvar ou aberta\nEscolha a opção:").upper()
                                        if c11 == "A":
                                            return "Família Passifloraceae"
                                        elif c11 == "B":
                                            c12 = input("A.Ovário unilocular\nB.Ovário bilocular\nEscolha a opção:").upper()
                                            if c12 == "A":
                                                return "Família Caricaceae"
                                            elif c12 == "B":
                                                return "Família Malvaceae"
                            elif c6 == "B":
                                c13 = input("A.Lóculos do ovário pluriovulados\nB.Óvulos 1-2 por lóculo do ovário\nEscolha a opção:").upper()
                                if c13 == "A":
                                    c14 = input("A.Prefloração do cálice imbricada\n.B.Prefloração do cálice valvar ou aberta\nEscolha a opção:").upper()
                                    if c14 == "A":
                                        return "Família Oxalidaceae"
                                    elif c14 == "B":
                                        return "Família Malvaceae"
                                elif c13 == "B":
                                    c15 = input("A.Gineceu tricarpelar\nB.Gineceu 4-20-carpelar\nEscolha a opção:").upper()
                                    if c15 == "A":
                                        c16 = input("A.Fruto carnoso\nB.Fruto Seco\nEscolha a opção:").upper()
                                        if c16 == "A":
                                            return "Família Sapotaceae"
                                        elif c16 == "B":
                                            return "Família Euphorbiaceae"
                                    elif c15 == "B":
                                        c17 = input("A.Folhas compostas\nB.Folhas simples ou compostas unifolioladas\nEscolha a opção:").upper()
                                        if c17 == "A":
                                            return "Família Oxalidaceae"
                                        elif c17 == "B":
                                            c18 = input("A.Arbustos ou árvores;lóculo do ovário com um único óvulo\nB.Ervas ou subarbustos;lóculos do ovário biovulados\nEscolha a opção:").upper()
                                            if c18 == "A":
                                                return "Família Sapotaceae"
                                            elif c18 == "B":
                                                return "Família Oxalidaceae"
            elif c3 == "B":
                c19 = input("A.Corola zigomorfa\nB.Corola actinomorfa\nEscolha a opção:").upper()
                if c19 == "A":
                    c20 = input("A.Estames em número superior ao das pétalas\nB.Estames em número igual ou inferior das pétalas\nEscolha a opção:").upper()
                    if c20 == "A":
                        return "Família Ericaceae"
                    elif c20 == "B":
                        c21 = input("A. Ovário unilocular\nB. Ovário bi-pentalocular ou gineceu dialicarpelar(ás vezes carpelos unidos pelos estiletes)\nEscolha a opção:").upper()
                        if c21 == "A":
                            c22 = input("A. Estames em número igual ao das pétalas\nB. Estames em número inferior aos das pétalas\nEscolha a opção:").upper()
                            if c22 == "A":
                                return "Família Apocynaceae"
                            elif c22 == "B":
                                c23 = input("A. Estames unidos pelas anteras\nB. Anteras livres entre si\nEscolha a opção:").upper()
                                if c23 == "A":
                                    return "Família Gesneriaceae"
                                elif c23 == "B":
                                    return "Família Bignoniaceae"
                        elif c21 == "B":
                            c24 = input("A. Gineceu pentacarpelar\nB. Gineceu bi-tetracarpelar\nEscolha a opção:").upper()
                            if c24 == "A":
                                c25 = input("A. Folhas simples, sem pontuações translúcidas; plantas herbáceas\nB. Folhas geralmente compostas,com pontuações translúcidas; plantas geralmente lenhosas\nEscolha a opção:").upper()
                                if c25 == "A":
                                    return "Família Balsaminaceae"
                                elif c25 == "B":
                                    return "Família Rutaceae"
                            elif c24 == "B":
                                c26 = input("A. Estilete ginobásico\nB. Estilete terminal\nEscolha a opção:").upper()
                                if c26 == "A":
                                    return "Família Lamiaceae(Labiatae)"
                                elif c26 == "B":
                                    c27 = input("A. Estames em número igual ao das pétalas\nB. Estames em número inferior ao das pétalas\nEscolha a opção:").upper()
                                    if c27 == "A":
                                        c28 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                                        if c28 == "A":
                                            return "Família Apocynaceae"
                                        elif c28 == "B":
                                            return "Família Solanaceae"
                                    elif c27 == "B":
                                        c29 = input("A. Folhas com pontuações translúcidas\nB. Folhas sem pontuações translúcidas\nEscolha a opção:").upper()
                                        if c29 == "A":
                                            return "Família Rutaceae"
                                        elif c29 == "B":
                                            c30 = input("A. Lóculos do ovário uni-biovulados\nB. Lóculos do ovário tri-pluriovulados\nEscolha a opção:").upper()
                                            if c30 == "A":
                                                c31 = input("A. Cálice muito reduzido, mas flores com 1-2 brácteas na base, semelhantes a um cálice\nB. Cpalice desenvolvido\nEscolha a opção:").upper()
                                                if c31 == "A":
                                                    return "Família Acanthaceae"
                                                elif c31 == "B":
                                                    c32 = input("A. Flores dispostas em inflorescências racemosas; óvulos com placentação ereta\nB. Flores dispostas em inflorescências cimosas ou racemosas; òvulos com placentação axial ou pêndula\nEscolha a opção:").upper()
                                                    if c32 == "A":
                                                        return "Família Verbenaceae"
                                                    elif c32 == "B":
                                                        return "Família Lamiaceae (Labiatae)"
                                            elif c30 == "B":
                                                c33 = input("A. Folhas alternas\nB. Folhas opostas ou verticiladas\nEscolha a opção:").upper()
                                                if c33 == "A":
                                                    return "Família Solanaceae"
                                                elif c33 == "B":
                                                    c34 = input("A. Folhas compostas\nB. Folhas simples\nEscolha a opção:").upper()
                                                    if c34 == "A":
                                                        return "Família Bignoniaceae"
                                                    elif c34 == "B":
                                                        c35 = input("A. Óvulos pouco numerosos, empilhados; fruto geralmente com retináculo(ejaculador)\nB. Óvulos muito numerosos, não empilhados; fruto sem ejaculador\nEscolha a opção:").upper()
                                                        if c35 == "A":
                                                            return "Família Acanthaceae"
                                                        elif c35 == "B":
                                                            c36 = input("A. Cálice dialissépalo\nB. Cálice gamossépalo\nEscolha a opção:").upper()
                                                            if c36 == "A":
                                                                return "Família Plantagianaceae"
                                                            elif c36 == "B":
                                                                return "Família Bignonieaceae"
                elif c19 == "B":
                    c37 = input("A. Ovário unilocular\nB. Ovário bi-plurilocular(ao menos na região mediana)\nEscolha a opção:").upper()
                    if c37 == "A":
                        c38 = input("A. Ovário com 1 ou 2 óvulos\nB. ovário com 3 a numerosos óvulos\nEscolha a opção:").upper()
                        if c38 == "A":
                            c39 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                            if c39 == "A":
                                return "Família Sapotaceae"
                            elif c39 == "B":
                                c40 = input("A. Gineceu pentacarpelar\nB. Gineceu 2-3-carpelar\nEscolha a opção:").upper()
                                if c40 == "A":
                                    return "Família Plumbaginaceae"
                                elif c40 == "B":
                                    return "Família Nyetaginaceae (na realidade monoclamídeas)"
                        elif c38 == "B":
                            c41 = input("A. Folhas opostas ou verticiladas\nB. Folhas alternas\nEscolha a opção:").upper()
                            if c41 == "A":
                                return "Família Apocynaceae"
                            elif c41 == "B":
                                c42 = input("A. Estames em número igual ao dobro das pétalas\nB. Estames em número inferior ao dobro das pétalas\nEscolha a opção:").upper()
                                if c42 == "A":
                                    return "Família Caricaceae"
                                elif c42 == "B":
                                    c43 = input("A. Óvulos com placentação central-livre ou basal\nB. Óvulos com placentação parietal\nEscolha a opção:").upper()
                                    if c43 == "A":
                                        return "Família Convolculaceae"
                                    elif c43 == "B":
                                        c44 = input("A. Gineceu bicarpelar, flor sem androginóforo\nB. Gineceu 3-4-carpelar; flor com androginóforo\nEscolha a opção:").upper()
                                        if c44 =="A":
                                            return "Família Apocynaceae"
                                        elif c44 == "B":
                                            return "Família Passifloraceae"
                    elif c37 == "B":
                        c45 = input("A. Lóculos do ovário 4-pluriovulados\nB. Lóculos do ovário uni-triovulados\nEscolha a opção:").upper()
                        if c45 == "A":
                            c46 = input("A. Estames 2-4\nB. Estames 5-numerosos\nEscolha a opção:").upper()
                            if c46 == "A":
                                c47 = input("A. Cálice dialissépalo\nB. Cálice gamossépalo\nEscolha a opção:").upper()
                                if c47 == "A":
                                    return "Família Clusiaceae (Guttiferae)"
                                elif c47 == "B":
                                    return "Família Solanaceae"
                            elif c46 == "B":
                                c48 = input("A. Estames 5-7\nB. Estames 8-numerosos\nEscolha a opção:").upper()
                                if c48 == "A":
                                    c49 = input("A. Plantas com látex\nB. Plantes sem látex\nEscolha a opção:").upper()
                                    if c49 == "A":
                                        c50 = input("A. Folhas opostas\nB. Folhas alternas\nEscolha a opção:").upper()
                                        if c50 == "A":
                                            return "Família Clusiaceae (Guttiferae)"
                                        elif c50 == "B":
                                            return "Família Caricaceae"
                                    elif c49 == "B":
                                        c51 = input("A. Gineceu pentacarpelar\nB. Gineceu 2-4-carpelar\nEscolha a opção:").upper()
                                        if c51 == "A":
                                            return "Família Caricaceae"
                                        elif c51 == "B":
                                            c52 = input("A. Gineceu tetracarpelar\nB. Gineceu 2-3-carpelar\nEscolha a opção:").upper()
                                            if c52 == "A":
                                                c53 = input("A. Cálice gamossépalo\nB. Cálice dialissépalo\nEscolha a opção:").upper()
                                                if c53 == "A":
                                                    return "Família Solanaceae"
                                                elif c53 == "B":
                                                    return "Família Convolvulaceae"
                                            elif c52 == "B":
                                                c54 = input("A. Folhas opostas ou verticiladas\nB. Folhas alternas\nEscolha a opção:").upper()
                                                if c54 == "A":
                                                    c55 = input("A. Todos os estames com o mesmo tamanho\nB. Estames com diferentes tamanhos\nEscolha a opção:").upper()
                                                    if c55 == "A":
                                                        return "Família Apocynaceae"
                                                    elif c55 == "B":
                                                        return "Família Solanaceae"
                                                elif c54 == "B":
                                                    c56 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                                                    if c56 == "A":
                                                        return "Família Apocynaceae"
                                                    elif c56 == "B":
                                                        c57 = input("A. Anteras poricidas\nB. Anteras rimosas\nEscolha a opção:").upper()
                                                        if c57 == "A":
                                                            return "Família Solanaceae"
                                                        elif c57 == "B":
                                                            c58 = input("A. Fruto baga\nB. Fruto cápsula\nEscolha a opção:").upper()
                                                            if c58 == "A":
                                                                return "Família Solanaceae"
                                                            elif c58 == "B":
                                                                c59 = input("A. Flores grandes, com mais de 3cm de comprimento\nB. Flores menores, com menos de 3 cm de comprimento\nEscolha a opção:").upper()
                                                                if c59 == "A":
                                                                    return "Família Solanaceae"
                                                                elif c59 == "B":
                                                                    return "Família Boraginaceae"
                                elif c48 == "B":
                                    c60 = input("A. Plantas suculentas\nB. Plantas não suculentas\nEscolha a opção:").upper()
                                    if c60 == "A":
                                        return "Família Crassulaceae"
                                    elif c60 == "B":
                                        c61 = input("A. Folhas compostas, com mais de um folíolo\nB. Folhas simples ou compostas unifolioladas\nEscolha a opção:").upper()
                                        if c61 == "A":
                                            return "Família Oxalidaceae"
                                        elif c61 == "B":
                                            c62 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                                            if c62 == "A":
                                                return "Família Clusiaceae (Guttiferae)"
                                            elif c62 == "B":
                                                return "Família Ericaceae" 
                        elif c45 == "B":
                            c63 = input("A. Folhas compostas\nB. Folhas simples ou compostas unifolioladas, ás vezes escamiformes\nEscolha a opção:").upper()
                            if c63 == "A":
                                c64 = input("A. Folhas opostas\nB. Folhas alternas\nEscolha a opção:").upper()
                                if c64 == "A":
                                    c65 = input("A. Folhas com pontuações translúcidas\nB. Folhas sem pontuações translúcidas\nEscolha a opção:").upper()
                                    if c65 == "A":
                                        return "Família Rutaceae"
                                    elif c65 == "B":
                                        return "Família Oleaceae"
                                elif c64 == "B":
                                    c66 = input("A. Estames unidos entre si\nB. Estames livres entre si\nEscolha a opção:").upper()
                                    if c66 == "A":
                                        c67 = input("A. Estames dispostos em dois cilos de diferentes alturas, sendo um destes, ás vezes, estaminodial\nB. Estames dispostos em um único ciclo\nEscolha a opção:").upper()
                                        if c67 == "A":
                                            return "Família Oxalidaceae"
                                        elif c67 == "B":
                                            c68 = input("A. Folhas geralmente sem pontuações translúcidas; fruto cápsula\nB. Folhas com pontuações translúcidas; fruto equizocárpico\nEscolha a opção:").upper()
                                            if c68 == "A":
                                                return "Família Meliaceae"
                                            elif c68 == "B":
                                                return "Família Rutaceae"
                                    elif c66 =="B":
                                        c69 = input("A. Folhas com pontuações translúcidas\nB. Folhas sem pontuações translúcidas\nEscolha a opção:").upper()
                                        if c69 == "A":
                                            return "Família Rutaceae"
                                        elif c69 == "B":
                                            return "Família Convolvulaceae"
                            elif c63 == "B":
                                c70 = input("A. Folhas com pontuações translúcidas\nB. Folhas sem pontuações translúcidas\nEscolha a opção:").upper()
                                if c70 == "A":
                                    return "Família Rutaceae"
                                elif c70 == "B":
                                    c71 = input("A. Estames unidos entre si\nB. Estames livres entre si\nEscolha a opção:").upper()
                                    if c71 == "A":
                                        c72 = input("A. Ervas\nB. Plantas lenhosas\nEscolha a opção:").upper()
                                        if c72 == "A":
                                            c73 = input("A. Estames 5, alternados com 5 estaminódios\nB. Estames 10\nEscolha a opção:").upper()
                                            if c73 == "A":
                                                return "Família Linaceae"
                                            elif c73 == "B":
                                                return "Família Oxalidaceae"
                                        elif c72 == "B":
                                            c74 = input("A. Folhas compostas\nB. Folhas simples\nEscolha a opção:").upper()
                                            if c74 == "A":
                                                return "Família Meliaceae"
                                            elif c74 == "B":
                                                return "Família Clusiaceae (Guttiferae)"
                                    elif c71 == "B":
                                        c75 = input("A. Estames 2\nB. Estames 4-numerosos\nEscolha a opção:").upper()
                                        if c75 == "A":
                                            return "Família Oleaceae"
                                        elif c75 == "B":
                                            c76 = input("A. Lóculos do ovário com um único óvulo\nB. Lóculos do ovário 2-4-ovulados\nEscolha a opção:").upper()
                                            if c76 == "A":
                                                c77 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                                                if c77 =="A":
                                                    c78 = input("A. Plantas herbáceas\nB. Plantas lenhosas\nEscolha a opção:").upper()
                                                    if c78 == "A":
                                                        return "Família Convolvulaceae"
                                                    elif c78 == "B":
                                                        return "Família Sapotaceae"
                                                elif c77 == "B":
                                                    c79 = input("A. Estilete ginobásico\nB. Estilete terminal\nEscolha a opção:").upper()
                                                    if c79 == "A":
                                                        return "Família Boraginaceae"
                                                    elif c79 == "B":
                                                        c80 = input("A. Cálice gamossépalo\nB. Cálice dialissépalo\nEscolha a opção:").upper()
                                                        if c80 == "A":
                                                            return "Família Boraginaceae"
                                                        elif c80 == "B":
                                                            return "Família Convolvulaceae"
                                            elif c76 == "B":
                                                c81 = input("A. Ervas ou lianas\nB. Arbustos ou árvores\nEscolha a opção:").upper()
                                                if c81 == "A":
                                                    c82 = input("A. Flores dispostas em inflorescências densas, secundifloras\nB. Flores solitárias ou dispostas em cimeiras ou panículas laxas\nEscolha a opção:").upper()
                                                    if c82 == "A":
                                                        return "Família Boraginaceae"
                                                    elif c82 == "B":
                                                        c83 = input("A. Flores com cinco estaminódios alternados com os estames\nB. Flores sem estaminódios\nEscolha a opção:").upper()
                                                        if c83 == "A":
                                                            return "Família Linaceae"
                                                        elif c83 == "B":
                                                            return "Família Convolvulaceae"
                                                elif c81 == "B":
                                                    c84 = input("A. Folhas opostas\nB. Folhas alternas\nEscolha a opção:").upper()
                                                    if c84 == "A":
                                                        return "Família Clusiaceae (Guttiferae)"
                                                    elif c84 == "B":
                                                        return "Família Ebenaceae"                                      
        elif c2 == "B":
            c85 = input("A.Folhas opostas ou verticiladas\nB.Folhas alternas\nEscolha a opção:").upper()
            if c85 == "A":
                c86 = input("A.Plantas com estípulas interpeciolares\nB.Plantas sem estípulas interpeciolares\nEscolha a opção:").upper()
                if c86 == "A":
                    return "Família Rubiaceae"
                elif c86 == "B":
                    c87 = input("A.Carpelos 3-10\nB.Carpelos 2\nEscolha a opção:").upper()
                    if c87 == "A":
                        c88 = input("A.Plantas hemiparasitas com haustórios\nB.Plantas não hemiparasitas\n\nEscolha a opção:").upper()
                        if c88 == "A":
                            return "Família Loranthaceae"
                        elif c88 == "B":
                            c89 = input("A.Carola rotácea, actinomorfa\nB.Corola tubulosa,geralmente zigomorfa\nEscolha a opção:").upper()
                            if c89 == "A":
                                return "Família Adoxaceae"
                            elif c89 == "B":
                                return "Família Caprifoliaceae"
                    elif c87 == "B":
                        c90 = input("A.Flores dispostas em capítulos\nB.Flores dispostas em outros tipos de inflorescências").upper()
                        if c90 == "A":
                            return "Asteraceae(Compositae)"
                        elif c90 == "B":
                            return "Gesneriaceae"
            elif c85 == "B":
                c91 = input("A.Plantas hemiparasitas\nB.Plantas não hemiparasitas\nEscolha a opção:").upper()
                if c91 == "A":
                    return "Família Loranthaceae"
                elif c91 == "B":
                    c92 = input("A.Ovário unilocular\nB.Ovário bi-plurilocular ou dialicarpelar\nEscolha a opção:").upper()
                    if c92 == "A":
                        c93 = input("A.Flores dispostas em capítulos\nB.Flores dispostas em outros tipos de inflorescências\nEscolha a opção:").upper()
                        if c93 == "A":
                            return "Família Asteraceae"
                        elif c93 == "B":
                            return "Família Cucurbitaceae"
                    elif c92 =="B":
                        c94=input("A.Corola com prefloração valvar\nB.Corola com prefloração imbricada ou convoluta\nEscolha a opção:").upper()
                        if c94=="A":
                            c95=input("A.Lóculos do ovário com um único óvulo\nB.Lóculos do ovário com dois a muitos óvulos\nEscolha a opção:").upper()
                            if c95=="A":
                                return "Família Araliaceae"
                            elif c95=="B":
                                return "Família Cucurbitaceae"
                        elif c94=="B":
                            c96=input("A.Flores unissexuadas\nB.Flores bissexuadas\nEscolha a opção:").upper()
                            if c96=="A":
                                return "Família Cucurbitaceae"
                            elif c96=="B":
                                c97=input("A.Estames 30-numerosos\nB.Estames 5\nEscolha a opção:").upper()
                                if c97=="A":
                                    return "Família Lecythidaceae"
                                elif c97=="B":
                                    return "Família Apocynaceae"


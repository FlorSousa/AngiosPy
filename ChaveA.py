def encontra_familia_chave_A ():
    print("CHAVE A: FLORES ACLAMÍDEAS OU MONOCLAMÍDEAS")
    c1=input("A.Flores aclamídeas\nB.Flores monoclamídeas\nEscolha a opção:").upper()
    if c1=="A":
        c2=input("A.Folhas opostas ou verticiladas\nB.Folhas alternas ou ausentes\nEscolha a opção:").upper()
        if c2=="A":
            c3=input("A.Folhas escamiformes\nB.Folhas não escamiformes\nEscolha a opção:").upper()
            if c3=="A":
                return "Família Casuarinaceae"
            elif c3=="B":
                c4=input("A.Plantas em geral com látex; ovário trilocular; fruto geralmente com deiscência explosiva (tricoca)\nB.Plantas sem látex; ovário unilocular; fruto indeiscente\nEscolha a opção:").upper()
                if c4=="A":
                    return "Família Euphorbiaceae"
                elif c4=="B":
                    return "Família Piperaceae"
        elif c2=="B":
            c5=input("A.Inflorescência do tipo espádice\nB.Inflorescência de outros tipos\nEscolha a opção:").upper()
            if c5=="A":
                return "Família Araceae"
            elif c5=="B":
                c6=input("A.Folhas paralelinérveas\nB.Folhas peninérveas ou palminérveas\nEscolha a opção:").upper()
                if c6=="A":
                    c7=input("A.Flores dispostas em espigas ou racemos\nB.Flores dispostas em espiguetas\nEscolha a opção:").upper()
                    if c7=="A":
                        return "Família Typhaceae"
                    elif c7=="B":
                        c8=input("A.Caule geralmente de seção triangular; folhas alternas espiraladas, com bainha geralmente fechada; fruto aquênio\nB.Caule geralmente de seção circular ou achatada; folhas alternas dísticas ou muito raramente espiraladas, com bainha geralmente aberta; fruto cariopse\nEscolha a opção:").upper()
                        if c8=="A":
                            return "Família Cyperaceae"
                        elif c8=="B":
                            return "Família Poaceae(Gramineae)"
                elif c6=="B":
                    c9=input("A.Plantas com látex\nB.Plantas sem látex\nEscolha a opção:").upper()
                    if c9=="A":
                        c10=input("A.Estípulas laterais; ovário com dois a três lóculos\nB.Estípulas terminais; ovário unilocular\nEscolha a opção:").upper()
                        if c10=="A":
                            return "Família Euphorbiaceae"
                        elif c10=="B":
                            return "Família Moraceae"
                    elif c9=="B":
                        c11=input("A.Flores geralmente sésseis e dispostas em espigas; ovário com um único óvulo\nB.Flores geralmente pediceladas e dispostas em outros tipos de inflorescências; ovário com dois a muitos óvulos\nEscolha a opção:").upper()
                        if c11=="A":
                            return "Família Piperaceae"
                        elif c11=="B":
                            return "Família Salicaceae"
    elif c1=="B":
        c12=input("A.Flores unissexuadas\nB.Flores bissexuadas\nEscolha a opção:").upper()
        if c12=="A":
            c13=input("A.Folhas opostas ou verticiladas\nB.Folhas alternas ou plantas afilas\nEscolha a opção:").upper()
            if c13=="A":
                c14=input("A.Ovário ínfero\nB.Ovário súpero\nEscolha a opção:").upper()
                if c14=="A":
                    c15=input("A.Ovário 2-5 locular\nB.Ovário unilocular\nEscolha a opção:").upper()
                    if c15=="A":
                        return "Família Rubiaceae"
                    elif c15=="B":
                        c16=input("A.Flores dispostas em inflorescências do tipo capítulo\nB.Flores solitárias ou dispostas em outros tipos de inflorescências\nEscolha a opção:").upper()
                        if c16=="A":
                            return "Família Asteraceae(Compositae)"
                        elif c16=="B":
                            return "Família Santalaceae"
                elif c14=="B":
                    c17=input("A.Estames em número igual ou maior ao das sépalas\nB.Estames em número menor do que as sépalas\nEscolha a opção:").upper()
                    if c17=="A":
                        c18=input("A.Ovário unilocular (às vezes por aborto)\nB.Ovário bi-plurilocular\nEscolha a opção:").upper()
                        if c18=="A":
                            c19=input("A.Gineceu unicarpelar (ou com dois carpelos, mas um deles extremamente reduzido)\nB.Gineceu bi-pluricarpelar\nEscolha a opção:").upper()
                            if c19=="A":
                                c20=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção:").upper()
                                if c20=="A":
                                    return "Família Urticaceae"
                                elif c20=="B":
                                    c21=input("A.Cálice dialissépalo\nB.Cálice gamossépalo\nEscolha a opção:").upper()
                                    if c21=="A":
                                        return "Família Clusiaceae(Guttiferae)"
                                    elif c21=="B":
                                        return "Família Nyctaginaceae"
                            elif c19=="B":
                                c22=input("A.Ovário com dois a muitos óvulos\nB.Ovário com um único óvulo\nEscolha a opção:").upper()
                                if c22=="A":
                                    return "Família Rubiaceae"
                                elif c22=="B":
                                    c23=input("A.Ervas\nB.Arbustos ou árvores\nEscolha a opção:").upper()
                                    if c23=="A":
                                        return "Família Amaranthaceae"
                                    elif c23=="B":
                                        c24=input("A.Óvulo com placentação pêndula\nB.Óvulo com placentação ereta\nEscolha a opção:").upper()
                                        if c24=="A":
                                            return "Família Moraceae"
                                        elif c24=="B":
                                            return "Família Clusiaceae(Guttiferae)"
                        elif c18=="B":
                            c25=input("A.Lóculos com dois a muitos óvulos\nB.Lóculos com um único óvulo\nEscolha a opção:").upper()
                            if c25=="A":
                                return "Família Sapindaceae"
                            elif c25=="B":
                                c26=input("A.Óvulos com placentação ereta ou pêndula\nB.Óvulos com placentação parietal ou axial\nEscolha a opção:").upper()
                                if c26=="A":
                                    return "Família Moraceae"
                                elif c26=="B":
                                    return "Família Euphorbiaceae"
                    elif c17=="B":
                        c27=input("A.Folhas compostas\nB.Folhas simples\nEscolha a opção:").upper()
                        if c27=="A":
                            return "Família Oleaceae"
                        elif c27=="B":
                            c28=input("A.Flor com dois ou mais pistilos\nB.Flor com um único pistilo\nEscolha a opção:").upper()
                            if c28=="A":
                                return "Família Siparunaceae"
                            elif c28=="B":
                                c29=input("A.Plantas com látex; folhas opostas, não escamiformes\nB.Plantas sem látex; folhas verticiladas, escamiformes\nEscolha a opção:").upper()
                                if c29=="A":
                                    return "Família Moraceae"
                                elif c29=="B":
                                    return "Família Casuarinaceae"
            elif c13=="B":
                c30=input("A.Ovário ínfero\nB.Ovário súpero\nEscolha a opção:").upper()
                if c30=="A":
                    c31=input("A.Plantas hemiparasitas\nB.Plantas hemiparasitas\nEscolha a opção:").upper()
                    if c31=="A":
                        return "Família Santalaceae"
                    elif c31=="B":
                        c32=input("A.Ovário unilocular\nB.Ovário bi-plurilocular, ao menos na região mediana do ovário\nEscolha a opção:").upper()
                        if c32=="A":
                            c33=input("A.Ovário com um único óvulo\nB.Ovário bi-pluriovulado\nEscolha a opção:").upper()
                            if c33=="A":
                                c34=input("A.Flores dispostas em capítulos\nB.Flores dispostas em inflorescências de outros tipos\nEscolha a opção:").upper()
                                if c34=="A":
                                    return "Família Asteraceae(Compositae)"
                                elif c34=="B":
                                    return "Família Moraceae"
                            elif c33=="B":
                                c35=input("A.Sépalas numerosas; folhas geralmente transformadas em espinhos\nB.Sépalas 2-9; folhas não transformadas em espinhos\nEscolha a opção:").upper()
                                if c35=="A":
                                    return "Família Cactaceae"
                                elif c35=="B":
                                    return "Família Combretaceae"
                        elif c32=="B":
                            c36=input("A.Lóculos do ovário com um único óvulo\nB.Lóculos do ovário com dois a muitos óvulos\nEscolha a opção:").upper()
                            if c36=="A":
                                return "Família Phytolaccaceae"
                            elif c36=="B":
                                c37=input("A.Plantas herbáceas\nB.Plantas lenhosas\nEscolha a opção:").upper()
                                if c37=="A":
                                    return "Família Begoniaceae"
                                elif c37=="B":
                                    return "Família Fagaceae"
                elif c30=="B":
                    c38=input("A.Gineceu bi-pluricarpelar\nB.Gineceu unicarpelar (ou bicarpelar com um dos carpelos extremamente reduzido)\nEscolha a opção:").upper()
                    if c38=="A":
                        c39=input("A.Ovário unilocular ou com um carpelo fértil e os demais estéreis\nB.Ovário bi-plurilocular\nEscolha a opção:").upper()
                        if c39=="A":
                            c40=input("A.Inflorescência do tipo espádice\nB.Inflorescência de outros tipos\nEscolha a opção:").upper()
                            if c40=="A":
                                return "Família Arecaceae(Palmae)"
                            elif c40=="B":
                                c41=input("A.Ovário com um único óvulo\nB.Ovário bi-pluriovulado\nEscolha a opção:").upper()
                                if c41=="A":
                                    c42=input("A.Folhas com bainha\nB.Folhas sem bainha\nEscolha a opção:").upper()
                                    if c42=="A":
                                        c43=input("A.Folhas alternas dísticas; flores dispostas em espigas; óvulo com placentação pêndula\nB.Folhas alternas espiraladas; flores dispostas em espiguetas; óvulo com placentação ereta\nEscolha a opção:").upper()
                                        if c43=="A":
                                            return "Família Typhaceae"
                                        elif c43=="B":
                                            return "Família Cyperaceae"
                                    elif c42=="B":
                                        c44=input("A.Plantas com látex\nB.Plantas sem látex\nEscolha a opção:").upper()
                                        if c44=="A":
                                            return "Família Moraceae"
                                        elif c44=="B":
                                            c45=input("A.Folhas com ócrea\nB.Folhas sem ócrea\nEscolha a opção:").upper()
                                            if c45=="A":
                                                return "Família Polygonaceae"
                                            elif c45=="B":
                                                c46=input("A.Estípulas ausentes\nB.Estípulas presentes\nEscolha a opção:").upper()
                                                if c46=="A":
                                                    return "Família Amaranthaceae"
                                                elif c46=="B":
                                                    c47=input("A.Óvulos com placentação ereta\nB.Óvulos com placentação pêndula\nEscolha a opção:").upper()
                                                    if c47=="A":
                                                        return "Família Urticaceae"
                                                    elif c47=="B":
                                                        return "Família Cannabaceae"
                                elif c41=="B":
                                    c48=input("A.Placentação ereta ou pêndula\nB.Placentação central-livre ou parietal\nEscolha a opção:").upper()
                                    if c48=="A":
                                        return "Família Amaranthaceae"
                                    elif c48=="B":
                                        return "Família Salicaceae"
                        elif c39=="B":
                            c49=input("A.Inflorescência do tipo espádice\nB.Inflorescência de outros tipos\nEscolha a opção:").upper()
                            if c49=="A":
                                c50=input("A.Ervas; espádice simples\nB.Palmeiras (geralmente lenhosas); espádice composto\nEscolha a opção:").upper()
                                if c50=="A":
                                    return "Família Araceae"
                                elif c50=="B":
                                    return "Família Arecaceae(Palmae)"
                            elif c49=="B":
                                c51=input("A.Folhas com bainha\nB.Folhas sem bainha\nEscolha a opção:").upper()
                                if c51=="A":
                                    return "Família Typhaceae"
                                elif c51=="B":
                                    c52=input("A.Lóculos do ovário com um único óvulo\nB.Lóculos do ovário com mais de um óvulo\nEscolha a opção:").upper()
                                    if c52=="A":
                                        c53=input("A.Ovário penta-plurilocular\nB.Ovário trilocular\nEscolha a opção:").upper()
                                        if c53=="A":
                                            return "Família Phytolaccaceae"
                                        elif c53=="B":
                                            return "Família Euphorbiaceae"
                                    elif c52=="B":
                                        c54=input("A.Lóculos do ovário tri-ovulados\nB.Lóculos do ovário bi-ovulados\nEscolha a opção:").upper()
                                        if c54=="A":
                                            return "Família Malvaceae"
                                        elif c54=="B":
                                            c55=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção:").upper()
                                            if c55=="A":
                                                return "Família Phyllanthaceae"
                                            elif c55=="B":
                                                return "Família Sapindaceae"
                    elif c38=="B":
                        c56=input("A.Plantas não lenhosas\nB.Plantas lenhosas\nEscolha a opção:").upper()
                        if c56=="A":
                            return "Família Urticaceae"
                        elif c56=="B":
                            c57=input("A.Plantas com látex\nB.Plantas sem látex\nEscolha a opção:").upper()
                            if c57=="A":
                                return "Família Moraceae"
                            elif c57=="B":
                                c58=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção:").upper()
                                if c58=="A":
                                    return "Família Urticaceae"
                                elif c58=="B":
                                    return "Família Nyctaginaceae"
        elif c12=="B":
            c59 = input("A. Ovário ínfero\nB. Ovário súpero\nEscolha a opção:").upper()
            if c59 == "A":
                c60 = input("A. Ovário unilocular\nB. Ovário bi-plurilocular\nEscolha a opção:").upper()
                if c60 == "A":
                    c61 = input("A. Flores dispostas em capítulos\nB. Flores solitárias ou dispostas em outros tipos de inflorescência\nEscolha a opção:").upper()
                    if c61 == "A":
                        return "Família Asteraceae(Compositae)"
                    elif c61 == "B":
                        c62 = input("A. Flores zigomorfas\nB. Flores actinomorfas\nEscolha a opção:").upper()
                        if c62 == "A":
                            return "Família Cactaceae"
                        elif c62 == "B":
                            c63 = input("A. Óvulos com placentação central-livre\nB. Óvulos com placentação pêndula, ereta ou parietal\nEscolha a opção:").upper()
                            if c63 == "A":
                                return "Família Portulacaceae"
                            elif c63 == "B":
                                c64 = input("A. Óvulos com placentação pêndula\nB. Óvulos com placentação ereta ou parieta\nEscolha a opção:").upper()
                                if c64 == "A":
                                    c65 = input("A. Gineceu unicarpelar\nB. Gineceu 2-5 carpelar\nEscolha a opção:").upper()
                                    if c65 == "A":
                                        return "Família Rosaceae"
                                    elif c65 == "B":
                                        c66 = input("A. Plantas herbáceas ou subarbustivas; hemiparasitas\nB. Plantas autótrofas, lenhosas\nEscolha a opção:").upper()
                                        if c66 == "A":
                                            return "Família Santalaceae"
                                        elif c66 == "B":
                                            return "Família Combretaceae"
                                elif c64 == "B":
                                    c67 = input("A. Sépalas numerosas; folhas geralmente transformadas em espinhos\nB. Sépalas 2-6; folhas não transformadas em espinhos\nEscolha a opção:").upper()
                                    if c67 == "A":
                                        return "Família Cactaceae"
                                    elif c67 == "B":
                                        "Família Portulacaceae"
                elif c60 == "B":
                    c68 = input("A. Plantas com estípulas interpeciolares\nB. Plantas sem estípulas ou com estípulas não interpeciolares\nEscolha a opção:").upper()
                    if c68 == "A":
                        return "Família Rubiaceae"
                    elif c68 == "B":
                        c69 = input("A. Flores zigomorfas\nB. Flores actinomorfas\nEscolha a opção:").upper()
                        if c69 == "A":
                            return "Família Aristolochiaceae"
                        elif c69 == "B":
                            c70 = input("A. Estames em número igual ou duplo ao das sépalas\nB. Estames numerosos\nEscolha a opção:").upper()
                            if c70 == "A":
                                c71 = input("A. Plantas lenhosas\nB. Plantas herbáceas\nEscolha a opção:").upper()
                                if c71 == "A":
                                    return "Plantas lenhosas"
                                elif c71 == "B":
                                    c72 = input("A. Folhas compostas ou sectas\nB. Folhas simples, inteiras\nEscolha a opção:").upper()
                                    if c72 == "A":
                                        return "Família Apiaceae(Umbelliferae)"
                                    elif c72 == "B":
                                        c73 = input("A.Flores pediceladas\nB. Flores sésseis\nEscolha a opção:").upper()
                                        if c73 == "A":
                                            return "Família Araliaceae"
                                        elif c73 == "B":
                                            return "Família Apiaceae(Umbelliferae)"
                            elif c70 == "B":
                                c74 = input("A. Florez zigomorfas\nB. Flores actinomorfas\nEscolha a opção:").upper()
                                if c74 == "A":
                                    return "Família Aristolochiaceae"
                                elif c74 == "B":
                                    c75 = input("A. Lianas\nB. Arbustos ou árvores\nEscolha a opção:").upper()
                                    if c75 == "A":
                                        return "Família Phytolaccaceae"
                                    elif c75 == "B":
                                        return "Família Myrtaceae"
            elif c59 == "B":
                c76 = input("A. Flor com dois ou mais pistilos\nB. Flor com único pistilo\nEscolha a opção:").upper()
                if c76 == "A":
                    c77 = input("A. Plantas sem estípulas\nB. Plantas com estípulas\nEscolha a opção:").upper()
                    if c77 == "A":
                        return "Família Phytolaccaceae"
                    elif c77 == "B":
                        c78 = input("A. Estípulas laterais\nB. Estípulas terminais\nEscolha a opção:").upper()
                        if c78 == "A":
                            return "Família Rosaceae"
                        elif c78 == "B":
                            return "Família Magnoliaceae"
                elif c76 == "B":
                    c79 = input("A. Ovário unilocular\nB. Ovário bi-plurilocular\nEscolha a opção:").upper()
                    if c79 == "A":
                        c80 = input("A. Ovário bi-pluriovulado\nB. Ovário com único óvulo\nEscolha a opção:").upper()
                        if c80 == "A":
                            c81 = input("A. Inflorescência do tipo espádice\nB. Inflorescência de outros tipos\nEscolha a opção:").upper()
                            if c81 == "A":
                                return "Família Araceae"
                            elif c81 == "B":
                                c82 = input("A. Folhas compostas bi-plurifolioladas\nB. Folhas simples, não pinatissectas, ou compostas unifolioladas\nEscolha a opção:").upper()
                                if c82 == "A":
                                    c83 = input("A. Gineceu bi-pluricarpelar\nB. Gineceu unicarpelar\nEscolha a opção:").upper()
                                    if c83 == "A":
                                        return "Família Rosaceae"
                                    elif c83 == "B":
                                        c84 = input("A. Plantas sem estípulas\nB. Plantas com estípulas\nEscolha a opção:").upper()
                                        if c84 == "A":
                                            return "Família Proteaceae"
                                        elif c84 == "B":
                                            c85 = input("A. Estames 8-12\nB. Estames 3-5\nEscolha a opção:").upper()
                                            if c85 == "A":
                                                return "Família Fabaceae(Leguminosae)"
                                            elif c85 == "B":
                                                return "Família Rosaceae"
                                elif c82 == "B":
                                    c86 = input("A. Óvulos com placentação central-livre\nB. Óvulos com placentação ereta, marginal, pêndula, parietal\nEscolha a opção:").upper()
                                    if c86 == "A":
                                        c87 = input("A. Flores períginas\nB. Flores hipóginas\nEscolha a opção:").upper()
                                        if c87 == "A":
                                            return "Família Lythraceae"
                                        elif c87 == "B":
                                            c88 = input("A. Folhas carnosas, alternas a opostas na mesma planta\nB. Folhas não carnosas; todas opostas\nEscolha a opção:").upper()
                                            if c88 == "A":
                                                return "Família Portulacaceae"
                                            elif c88 == "B":
                                                return "Família Caryophyllaceae"
                                    elif c86 == "B":
                                        c89 = input("A. Óvulos com placentação parietal ou marginal\nB. Óvulos com placentação ereta ou pêndula\nEscolha a opção:").upper()
                                        if c89 == "A":
                                            c90 = input("A. Sépalas numerosas\nB. Sépalas 1-12\nEscolha a opção:").upper()
                                            if c90 == "A":
                                                return "Família Cactaceae"
                                            elif c90 == "B":
                                                c91 = input("A. Gineceu unicarpelar\nB. Gineceu 2-18-carpelar\nEscolha a opção:").upper()
                                                if c91 == "A":
                                                    c92 = input("A. Folhas simples\nB. Folhas compostas unifolioladas\nEscolha a opção:").upper()
                                                    if c92 == "A":
                                                        return "Família Proteaceae"
                                                    elif c92 == "B":
                                                        return "Família Fabaceae(Leguminosae)"
                                                elif c91 == "B":
                                                    c93 = input("A. Plantas geralmente trepadeiras, flores geralmente com androginóforo\nB. Árvores ou arbustos, sem androginóforo\nEscolha a opção:").upper()
                                                    if c93 == "A":
                                                        return "Família Passifloraceae"
                                                    elif c93 == "B":
                                                        return "Família Saliaceae"
                                        elif c89 == "B":
                                            c94 = input("A. Óvulos com placentação pêndula\nB. Óvulos com placentação ereta\nEscolha a opção:").upper()
                                            if c94 == "A":
                                                return "Família Protaceae"
                                            elif c94 == "B":
                                                c95 = input("A. Flores escariosas; gineceu bicarpelar\nB. Flores não escariosas; gineceu tricarpelar\nEscolha a opção:").upper()
                                                if c95 == "A":
                                                    return "Família Amaranthaceae"
                                                elif c95 == "B":
                                                    return "Família Portulacaceae"
                        elif c80 == "B":
                            c96 = input("A. Inflorescência do tipo espádice\nB. Inflorescência de outros tipos\nEscolha a opção:").upper()
                            if c96 == "A":
                                return "Família Araceae"
                            elif c96 == "B":
                                c97 = input("A. Plantas com estípulas, ás vezes transformadas em ócrea ou em espinhos\nB. Plantas sem estípulas\nEscolha a opção:").upper()
                                if c97 == "A":
                                    c98 = input("A. Plantas com ócrea\nB. Plantas sem ócrea\nEscolha a opção:").upper()
                                    if c98 == "A":
                                        return "Família Polygonaceae"
                                    elif c98 == "B":
                                        c99 = input("A. Estames 1-9\nB. Estames 10-numerosos\nEscolha a opção:").upper()
                                        if c99 == "A":
                                            c100 = input("A. Folhas compostas\nB. Folhas simples\nEscolha a opção:").upper()
                                            if c100 == "A":
                                                return "Família Rosaceae"
                                            elif c100 == "B":
                                                c101 = input("A. Flores bissexuadas\nB. Flores unissexuadas\nEscolha a opção:").upper()
                                                if c101 == "A":
                                                    return "Família Phytolaccaceae"
                                                elif c101 == "B":
                                                    return "Família Urticaceae"
                                        elif c99 == "B":
                                            c102 = input("A. Folhas compostas\nB. Folhas simples\nEscolha a opção:").upper()
                                            if c102 == "A":
                                                return "Família Fabaceae(Leguminosae)"
                                            elif c102 == "B":
                                                return "Família Phytolaccaceae"
                                elif c97 == "B":
                                    c103 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção:").upper()
                                    if c103 == "A":
                                        return "Família Clusiaceae(Guttiferae)"
                                    elif c103 == "B":
                                        c104 = input("A. Cálice escarioso\nB. Cálice não escarioso, petaloide\nEscolha a opção:").upper()
                                        if c104 == "A":
                                            return "Família Amaranthaceae"
                                        elif c104 == "B":
                                            c105 = input("A. Cálice dialissépalo\nB. Cálice gamossépalo\nEscolha a opção:").upper()
                                            if c105 == "A":
                                                return "Família Phytolaccaceae"
                                            elif c105 == "B":
                                                c106 = input("A. Cálice unido apenas na base\nB. Cálice unido na maior parte de sua extensão, formando um tubo longo\nEscolha a opção:").upper()
                                                if c106 == "A":
                                                    return "Família Polygonaceae"
                                                elif c106 == "B":
                                                    return "Família Nyctaginaceae"
                    elif c79 == "B":
                        c107 = input("A. Inflorescência do tipo espádice\nB. Inflorescência de outros tipos\nEscolha a opção:").upper()
                        if c107 == "A":
                            c108 = input("A. Ervas; espádice simples\nB. Palmeiras(geralmente lenhosas); espádice composto\nEscolha a opção:").upper()
                            if c108 == "A":
                                return "Família Araceae"
                            elif c108 == "B":
                                return "Família Arecaceae(Palmae)"
                        elif c107 == "B":
                            c109 = input("A. Estame 1\nB. Estames 2-numerosos\nEscolha a opção:").upper()
                            if c109 == "A":
                                return "Família Lythraceae"
                            elif c109 == "B":
                                c110 = input("A. Lóculos do ovário uni-biovulados\nB. Lóculos do ovário tri-pluriovulados\nEscolha a opção:").upper()
                                if c110 == "A":
                                    c111 = input("A. Folhas compostas\nB. Folhas simples ou compostas unifolioladas\nEscolha a opção:").upper()
                                    if c111 == "A":
                                        return "Família Sapindaceae"
                                    elif c111 == "B":
                                        c112 = input("A. Lóculos do ovário biovulados\nB. Lóculos do ovário com único óvulo \nEscolha a opção:").upper()
                                        if c112 == "A":
                                            c113 = input("A. Plantas com estípulas\nB. Plantas sem estípulas\nEscolha a opção:").upper()
                                            if c113 == "A":
                                                return "Família Malvaceae"
                                            elif c113 == "B":
                                                return "Família Sapindaceae"
                                        elif c112 == "B":
                                            c114 = input("A. Carpelos 4-numerosos\nB. Carpelos 2-3\nEscolha a opção:").upper()
                                            if c114 == "A":
                                                return "Família Phytollaccaceae"
                                            elif c114 == "B":
                                                c115 = input("A. Óvulo com placentação pêndula\nB. Óvulo com placentação ereta\nEscolha a opção:").upper()
                                                if c115 == "A":
                                                    return "Família Ulmaceae"
                                                elif c115 == "B":
                                                    return "Família Rhamnaceae"
                                elif c110 == "B":
                                    c116 = input("A. Plantas lenhosas\nB. Plantas herbáceas\nEscolha a opção:").upper()
                                    if c116 == "A":
                                        return "Família Malvaceae"
                                    elif c116 == "B":
                                        c117 = input("A. Flores períginas\nB. Flores hipóginas\nEscolha a opção:").upper()
                                        if c117 == "A":
                                            return "Família Lythraceae"
                                        elif c117 == "B":
                                            return "Família Acanthaceae"
def encontra_familia_chave_B():
    c1 = input("A. Flores com 1-3 pétalas\nB. Flores com 4 ou mais pétalas\nEscolha a opção:").upper()
    if c1 == "A":
        c2 = input("A. Flores homoclamídeas\nB. Flores heteroclamídeas\n Escolha a opção:").upper()
        if c2 == "A":
            c3 = input("A. Perianto zigomorfo\nB. Perianto actinomorfo\n Escolha a opção:").upper()
            if c3 == "A":
                c4 = input("A. Estame 1, sem estaminódios\nB. Estames 2-numerosos ou 1 mais dois estaminódios\nEscolha a opção:").upper()
                if c4 == "A":
                    return "Família Orchidaceae"
                elif c4 == "B":
                    c5 = input("A. Estames 1-3\nB. Estames 5-numerosos\nEscolha a opção:").upper()
                    if c5 == "A":
                        return "Família Iridaceae"
                    elif c5 == "B":
                        c6 = input("A. Folhas peniparalelinérveas\nB.Folhas enérveas, uninérveas ou paralelinérveas, ás vezes extremamente reduzidas\nEscolha a opção:").upper()
                        if c6 == "A":
                            c7 = input("A. Folhas alternas espiraladas; fruto baga\nB. Folhas alternas dísticas; fruto drupa\nEscolha a opção:").upper()
                            if c7 == "A":
                                return "Família Musaceae"
                            elif c7 == "B":
                                return "Família Heliconiaceae"
                        elif c6 == "B":
                            c8 = input("A. Ovário súpero\nB. Ovário ínfero\nEscolha a opção:").upper()
                            if c8 == "A":
                                c9 = input("A. Plantas fibrosas\nB. Plantas não fibrosas\nEscolha a opção:").upper()
                                if c9 == "A":
                                    return "Família Agavaceae"
                                elif c9 == "B":
                                    c10 = input("A. Folhas suculentas\nB. Folhas não suculentas\nEscolha a opção:").upper()
                                    if c10 == "A":
                                        return "Família Asphodelaceae"
                                    elif c10 == "B":
                                        return "Família Hemerocallidaceae"
                            elif c8=="B":
                                c11 = input("A. Plantas lenhosas\nB. Plantas herbáceas\nEscolha a opção:").upper()
                                if c11 == "A":
                                    return "Família Agavaceae"
                                elif c11 == "B":
                                    return "Família Amaryllidaceae"
            elif c3 == "B":
                c12 = input("A. Ervas geralmente aclorofiladas, holoparasitas\nB. Plantas autótrofas, clorofiladas\nEscolha a opção:").upper()
                if c12 == "A":
                    return "Família Lauraceae"
                elif c12 == "B":
                    c13 = input("A. Ovária súpero\nB. Ovário ínfero\nEscolha a opção:").upper()
                    if c13 == "A":
                        c14 = input("A. Plantas afilas ou com folhas reduzidas a escamas\nB. Plantas com folhas não reduzidas a escamas\nEscolha a opção:").upper()
                        if c14 == "A":
                            return "Família Asparagaceae"
                        elif c14 == "B":
                            c15 = input("A. Folhas opostas ou verticiladas\nB. Folhas alternas\nEscolha a opção:").upper()
                            if c15 == "A":
                                return "Família Lauraceae"
                            elif c15 == "B":
                                c16 = input("A. Folhas com gavinha no ápice\nB. Folhas sem gavinha\nEscolha a opção:").upper()
                                if c16 == "A":
                                    return "Família Colchicaceae"
                                elif c16 == "B":
                                    c17 = input("A. Plantas lenhosas\nB. Plantas não lenhosas\nEscolha a opção:").upper()
                                    if c17 == "A":
                                        c18 = input("A. Anteras valvares\nB. Anteras rimosas\nEscolha a opção:").upper()
                                        if c18 == "A":
                                            return "Família Lauraceae"
                                        elif c18 == "B":
                                            c19 = input("A. Folhas peninérveas\nB. Folhas paralelinérveas ou enérveas\nEscolha a opção:").upper()
                                            if c19 == "A":
                                                return "Família Annonaceae"
                                            elif c19 == "B":
                                                c20 = input("A. Folhas suculentas, não fibrosas\n B. Folhas não suculentas, geralmente fibrosas\nEscolha a opção:").upper()
                                                if c20 == "A":
                                                    return "Família Asphodelaceae"
                                                elif c20 == "B":
                                                    c21 = input("A. Ovário com lóculos pluriovulados\nB. Ovários com lóculos 2-8- ovulados\nEscolha a opção:").upper()
                                                    if c21 == "A":
                                                        return "Família Agavaceae"
                                                    elif c21 == "B":
                                                        return "Família Ruscaceae"
                                    elif c17 == "B":
                                        c22 = input("A. Plantas não bulbosas\nB. Plantas Bulbosas\nEscolha a opção:").upper()
                                        if c22 == "A":
                                            c23 = input("A. Folhas fibrosas\nB. Folhas não fibrosas\nEscolha a opção:").upper()
                                            if c23 == "A":
                                                c24 = input("A. Ovário com lóculos pluriovulados\nB. Ovário com lóculos 2-8-ovulados\nEscolha a opção:").upper()
                                                if c24 == "A":
                                                    return "Família Agavaceae"
                                                elif c24 == "B":
                                                    return "Família Ruscaceae"
                                            elif c23 == "B":
                                                c25 = input("A. Folhas suculentas\nB. Folhas não suculentas\nEscolha a opção:").upper()
                                                if c25 == "A":
                                                    return "Família Asphodelaceae"
                                                elif c25 == "B":
                                                    c26 = input("A. Flores dispostas em umbelas\nB. Flores dispostas em fascículos, racemos, cimeiras ou racemos de cimeiras\nEscolha a opção:").upper()
                                                    if c26 == "A":
                                                        return "Família Agapanthaceae"
                                                    elif c26 == "B":
                                                        c27 = input("A. Cálice e corola unidos, formando um tubo com mais de 1cm na base da flor\nB. Cálice e corola livres entre si ou unidos apenas muito próximo da base\nEscolha a opção:").upper()
                                                        if c27 == "A":
                                                            return "Família Hemerocallidaceae"
                                                        elif c27 == "B":
                                                            return "Família Asparagaceae"
                                        elif c22 == "B":
                                            c28 = input("A. Folhas dispostas ao longo do caule, sem a formação de um espaço\nB. Folhas dispostas em rosetas basais, flores dispostas na extremidade de um espaço\nEscolha a opção:").upper()
                                            if c28 == "A":
                                                return "Família Liliaceae"
                                            elif c28 == "B":
                                                return "Família Alliaceae"
                    elif c13 == "B":
                        c29 = input("A. Folhas alternas dísticas\nB. Plantas com uma única folha ou folhas alternas espiraladas\nEscolha a opção:").upper()
                        if c29 == "A":
                            c30 = input("A. Estames5-6\nB. Estames 1-3\nEscolha a opção:").upper()
                            if c30 == "A":
                                return "Família Amaryllidaceae"
                            elif c30 == "B":
                                return "Família Iridaceae"
                        elif c29 == "B":
                            c31 = input("A. Folhas com ápice pungente e com margem geralmente epinescente\nB. Folhas com ápice não pungente e com margem não espinescente\nEscolha a opção:").upper()
                            if c31 == "A":
                                return "Família Agavaceae"
                            elif c31 == "B":
                                c32 = input("A. Plantas com bulbos\nB. Plantas com cormos ou rizomas ou sem sistemas subterrâneos de reserva\nEscolha a opção: ").upper()
                                if c32 == "A":
                                    return "Família Amaryllidaceae"
                                elif c32 == "B":
                                    return "Família Hypoxidaceae"
        elif c2 == "B":
            c33 = input("A. Ovário ínfero\nB. Ovário súpero\nEscolha a opção:").upper()
            if c33 == "A":
                c34 = input("A. Flores actinomorfas\nB. Flores zigomorfas ou assimétricas\nEscolha a opção:").upper()
                if c34 == "A":
                    c35 = input("A. Folhas alternas\nB. Folhas opostas ou verticiladas\nEscolha a opção:").upper()
                    if c35 == "A":
                        c36 = input("A. Folhas perninérveas\nB. Folhas paralelinérveas ou uninérveas\nEscolha a opção:").upper()
                        if c36 == "A":
                            return "Família Begoniaceae"
                        elif c36 == "B":
                            c37 = input("A. Estames 3\nB. Estames 5-6\nEscolha a opção:").upper()
                            if c37 == "A":
                                return "Família Iridaceae"
                            elif c37 == "B":
                                return "Família Bromoliaceae"
                    elif c35=="B":
                        c38 = input("A. Corola dialipétala\nB. Corola gamopétala\nEscolha a opção: ").upper()
                        if c38 == "A":
                            return "Família Melastomataceae"
                        elif c38 == "B":
                            c39 = input("A. Plantas com estípulas interpeciolares; anteras livres entre si\nB. Plantas sem estípulas; anteras unidas entre si\nEscolha a opção: ").upper()
                            if c39 == "A":
                                return "Família Rubiaceae"
                            elif c39 == "B":
                                return "Família Asteraceae(Compositae)"
                elif c34=="B":
                    c40 = input("A. Flores assimétricas, graças á presença de um estame com uma das tecas petalóide\nB. Flores zigomorfas\nEscolha a opção: ").upper()
                    if c40 == "A":
                        c41 = input("A. Ovário com lóculos pluriovulados\nB. Lóculos do óvario com um único óvulo\nEscolha a opção: ").upper()
                        if c41 == "A":
                            return "Família Cannaceae"
                        elif c41 == "B":
                            return "Família Marantaceae"
                    elif c40 == "B":
                        c42 = input("A. Androceu unido ao gineceu, formando uma coluna\nB. Androceu não unido ao gineceu\nEscolha a opção: ").upper()
                        if c42 == "A":
                            return "Família Orchidaceae"
                        elif c42 == "B":
                            c43 = input("A. Estames 1-4\nB. Estames 5-6\nEscolha a opção: ").upper()
                            if c43 == "A":
                                c44 = input("A. Folhas alternas dísticas\nB. Folhas alternas espiraladas\nEscolha a opção: ").upper()
                                if c44 == "A":
                                    return "Família Zingiberaceae"
                                elif c44 == "B":
                                    return "Família Costaceae"
                            if c43 == "B":
                                c45 = input("A. Folhas alternas dísticas\nB. Folhas alternas espiraladas\nEscolha a opção: ").upper()
                                if c45 == "A":
                                    c46 = input("A. Lóculos do ovário com um único óvulo\nB. Ovário com lóculos pluriovulados\nEscolha a opção: ").upper()
                                    if c46 == "A":
                                        return "Família Heliconiaceae"
                                    elif c46 == "A":
                                        return "Família Strelitziaceae"
                                elif c45 == "B":
                                    c47 = input("A. Bainhas foliares formando um pseudocaule; sépalas unidas a duas pétalas, uma das pétalas livres\nB. Bainhas foliares não formando um pseudocaule; sépalas e pétalas livres entre si ou todas unidas\nEscolha a opção: ").upper()
                                    if c47 == "A":
                                        return "Família Musaceae"
                                    elif c47 == "B":
                                        return "Família Bromeliaceae"
            elif c33=="B":
                c48 = input("A. Folhas opostas ou verticiladas\nB. Folhas alternas ou rosuladas\nEscolha a opção: ").upper()
                if c48 == "A":
                    return "Família Lauraceae"
                elif c48 == "B":
                    c49 = input("A. Folhas ou folíolos paralelinérveos ou uninérveos\nB. Folhas ou folíolos palminérveos ou peninérveos\nEscolha a opção: ").upper()
                    if c49 == "A":
                        c50 = input("A. Plantas geralmente lenhosas; flores dispostas em espádice composto\nB. Plantas geralmente hérbaceas ou subarbustivas; flores dispostas em outros tipos de inflorescência\nEscolha a opção: ").upper()
                        if c50 == "A":
                            return "Família Arecaceae(Palmae)"
                        elif c50 == "B":
                            c51 = input("A. Folhas não formando rosetas; corola dialipétala\nB. Folhas formando rosetas; corola geralmenta gamopétala\nEscolha a opção: ").upper()
                            if c51 == "A":
                                return "Família Commelinaceae"
                            elif c51 == "B":
                                return "Família Bromelinaceae"
                    elif c49 == "B":
                        c52 = input("A. Anteras valvares\nB. Anteras rimosas\nEscolha a opção: ").upper()
                        if c52 == "A":
                            return "Família Lauraceae"
                        elif c52 == "B":
                            c53 = input("A. Folhas alternas dísticas\nB. Folhas alternas espiraladas\nEscolha a opção: ").upper()
                            if c53 == "A":
                                return "Família Annonaceae"
                            elif c53 == "B":
                                return "Família Fabaceae(Leguminosae)"
    elif c1=="B":
        c54=input("A.Ovário Ínfero\nB.Ovário Súpero\nEscolha a opção: ").upper()
        if c54=="A":
            c55=input("A.Pétalas numerosas\nB.Plantas cultivadas, cujo número de pétalas é resultado de melhoramento genético\nC.Pétalas 4-9 ou formando caliptra\nEscolha a opção: ").upper()
            if c55=="A":
                c56=input("A.Plantas aquáticas, não suculentas\nB.Plantas terrestres ou epíficas, suculentas\nEscolha a opção: ").upper()
                if c56=="A":
                    return "Família Nymphaeaceae"
                elif c56=="B":
                    return "Família Cactaceae(na realidade são monoclamídeas)"
            elif c55=="B" or c55=="C":
                c57=input("A.Folhas opostas ou verticiladas\nB.Folhas alternas\nEscolha a opção: ").upper()
                if c57=="A":
                    c58=input("A.Plantas hemiparasitas\nB.Plantas não hemiparasitas\nEscolha a opção: ").upper()
                    if c58=="A":
                        return "Família Loranthaceae"
                    elif c58=="B":
                        c59=input("A.Ovário unilocular\nB.Ovário bi-plurilocular\nEscolha a opção: ").upper()
                        if c59=="A":
                            c60=input("A.Folhas peninérveas; óvulos 2-6\nB.Folhas curvinérveas ou uninérveas; óvulos numerosos\nEscolha a opção: ").upper()
                            if c60=="A":
                                return "Família Combretaceae"
                            elif c60=="B":
                                return "Família Melastomataceae"
                elif c57=="B":
                    c66=input("A.Estames em número igual ou inferior ao das pétalas\nB.Estames em número maior que o das pétalas\nEscolha a opção: ").upper()
                    if c66=="A":
                        c67=input("A.Ovário unilocular\nB.Ovário 2-plurilocular\nEscolha a opção: ").upper()
                        if c67=="A":
                            c68=input("A.Flores unissexuadas\nB.Flores bissexuadas\nEscolha a opção: ").upper()
                            if c68=="A":
                                return "Família Curcubitaceae"
                            elif c68=="B":
                                c69=input("A.Plantas hemiparasitas\nB.Plantas não hemiparasitas\nEscolha a opção: ").upper()
                                if c69=="A":
                                    return "Família Loranthaceae"
                                elif c69=="B":
                                    return "Família Portulacaceae"
                        if c67=="B":
                            c70=input("A.Plantas lenhosas\nB.Plantas herbáceas\nEscolha a opção: ").upper()
                            if c70=="A":
                                return "Família Araliaceae"
                            elif c70=="B":
                                c71=input("A.Folhas compostas ou sectas\nB.Folhas simples inteiras\nEscolha a opção: ").upper()
                                if c71=="A":
                                    return "Família Apiaceae(Umbelliferae)"
                                elif c71=="B":
                                    c72=input("A.Brácteas ausentes ou inconspícuas\nB.Brácteas conspícuas dispostas na base da umbela\nEscolha a opção: ").upper()
                                    if c72=="A":
                                        return "Família Araliaceae"
                                    elif c72=="B":
                                        return "Família Apiaceae(Umbelliferae)"
                    elif c66=="B":
                        c73=input("A.Ovário unilocular\nB.Ovário bi-plurilocular(carpelos às vezes apenas parcialmente unidos)\nEscolha a opção: ").upper()
                        if c73=="A":
                            c74=input("A.Plantas lenhosas ou com folhas transformadas em espinhos\nB.Plantas herbáceas com folhas não transformadas em espinhos\nEscolha a opção: ").upper()
                            if c74=="A":
                                return "Família Cactaceae(na realidade monoclamídeas)"
                            elif c74=="B":
                                return "Família Portulacaceae"
                        if c73=="B":
                            c75=input("A.Lóculos 1-2-ovulados\nB.Lóculos 3-pluriovulados\nEscolha a opção: ").upper()
                            if c75=="A":
                                c76=input("A.Estames livres entre si; hipanto carnoso na frutificação, formando um pseudofruto do tipo pomo\nB.Estames unidos; fruto seco, sem formação de pseudofruto\nEscolha a opção: ").upper()
                                if c76=="A":
                                    return "Família Rosaceae"
                                elif c76=="B":
                                    return "Família Lecythidaceae"
                            elif c75=="B":
                                c77=input("A.Folhas com pontuações translúcidas\nB.Folhas sem pontuações translúcidas\nEscolha a opção: ").upper()
                                if c77=="A":
                                    return "Família Myrtaceae"
                                elif c77=="B":
                                    c78=input("A.Flores unissexuadas\nB.Flores bissexuadas\nEscolha a opção: ").upper()
                                    if c78=="A":
                                        return "Família Begoniaceae"
                                    elif c78=="A":
                                        c79=input("A.Estames em número duplo ao das pétalas\nB.Estames mais numerosos\nEscolha a opção: ").upper()
                                        if c79=="A":
                                            return "Família Onagraceae"
                                        elif c79=="B":
                                            c80=input("A.Estames livres entre si\nB.Estames unidos entre si\nEscolha a opção: ").upper()
                                            if c80=="A":
                                                return "Família Rosaceae"
                                            elif c80=="B":
                                                return "Família Lecythidaceae"
        elif c54=="B":
            c81=input("A.Flor com mais de um pistilo, às vezes unidos pelos estiletes\nB.Flor com um único pistilo\nEscolha a opção: ").upper()
            if c81=="A":
                c82=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção: ").upper()
                if c82=="A":
                    c83=input("A.Plantas com estípulas terminais\nB.Plantas com estípulas laterais ou interpeciolares\nEscolha a opção: ").upper()
                    if c83=="A":
                        return "Família Magnoliaceae"
                    elif c83=="B":
                        c84=input("A.Folhas compostas\nB.Folhas simples\nEscolha a opção: ").upper()
                        if c84=="A":
                            c85=input("A.Flores períginas ou hipóginas; cálice com perfloração valvar\nB.Flores hipóginas; cálice com perfloração imbricada\nEscolha a opção: ").upper()
                            if c85=="A":
                                return "Família Rosaceae"
                            elif c85=="B":
                                return "Família Ranunculaceae"
                        elif c84=="B":
                            c88=input("A. Estames em número inferior ou igual ao duplo ao das pétalas\nB. Estames numerosos\nEscolha a opção: ").upper()
                            if c88 == "A":
                                c89 = input("A. Folhas com pontuações translúcidas, ás vezes apenas na margem da folha\nB. Folhas sem pontuações translúcidas\nEscolha a opção: ").upper()
                                if c89 == "A":
                                    return "Família Rutaceae"
                                elif c89 == "B":
                                    return "Família Crassulaceae"
                            elif c88 == "B":
                                c90 = input("A. Flor calcarada\nB. Flor não calcarada\nEscolha a opção: ").upper()
                                if c90 == "A":
                                    return "Família Ranunculaceae"
                                elif c90 == "B":
                                    return "Família Rosacae"
            elif c81=="B":
                c91=input("A.Flor tetrâmera, com seis estames\nB.Flor não tetrâmera ou, se tetrâmera, com mais ou menos de seis estames\nEscolha a opção: ").upper()
                if c91=="A":
                    return "Família Brassicaceae(Cruciferae)"
                elif c91=="B":
                    c92=input("A. Ovário unilocular\nB. Ovário bi-plurilocular, ao menos na região mediana\nEscolha a opção: ").upper()
                    if c92 == "A":
                        c93=input("A.Ovário com um único óvulo\nB.Óvulos 2-numerosos\nEscolha a opção: ").upper()
                        if c93=="A":
                            c94=input("A.Placentação pêndula, axial, parietal ou marginal\nB.Placentação ereta ou central-livre\nEscolha a opção: ").upper()
                            if c94=="A":
                                c95=input("A.Plantas sem estípulas\nB.Plantas com estípulas\nEscolha a opção: ").upper()
                                if c95=="A":
                                    return "Família Anacardiaceae"
                                elif c95=="B":
                                    c96=input("A.Flores actinomorfas\nB.Flores zigomorfas\nEscolha a opção: ").upper()
                                    if c96=="A":
                                        c97=input("A.Plantas com látex\nB.Plantas sem látex\nEscolha a opção: ").upper()
                                        if c97=="A":
                                            return "Família Euphorbiaceae"
                                        elif c97=="B":
                                            return "Família Fabaceae(Leguminosae)"
                                    elif c96=="B":
                                        c98=input("A.Estames 10-numerosos\nB.Estames 4-8\nEscolha a opção: ").upper()
                                        if c98=="A":
                                            return "Família Fabaceae(Leguminosae)"
                                        elif c98=="B":
                                            return "Família Violaceae"
                            elif c94=="B":
                                c99=input("A.Estames 1-10\nB.Estames numerosos\nEscolha a opção: ").upper()
                                if c99=="A":
                                    c100=input("A.Plantas sem estípulas\nB.Plantas com estípulas\nEscolha a opção: ").upper()
                                    if c100=="A":
                                        return "Família Anacardiaceae"
                                    elif c100=="B":
                                        c101=input("A.Folhas compostas\nB.Folhas simples\nEscolha a opção: ").upper()
                                        if c101=="A":
                                            return "Família Fabaceae(Leguminosae)"
                                        elif c101=="B":
                                            return "Família Chrysobalanaceae"
                                elif c99=="B":
                                    c102=input("A.Folhas compostas\nB.Folhas simples\nEscolha a opção: ").upper()
                                    if c102=="A":
                                        return "Família Fabaceae(Leguminosae)"
                                    elif c102=="B":
                                        c103=input("A.Folhas opostas\nB.Folhas alternas\nEscolha a opção: ").upper()
                                        if c103=="A":
                                            return "Família Clusiaceae(Guttiferae)"
                                        elif c103=="B":
                                            c104=input("A.Gineceu 5-8 carpelar\nB.Gineceu unicarpelar\nEscolha a opção: ").upper()
                                            if c104=="A":
                                                return "Família Rosaceae"
                                            elif c104=="B":
                                                return "Família Fabaceae(Leguminosae)"
                        elif c91=="B":
                            c105=input("A.Flores zigomorfas ou assimétricas\nB.Flores actinomorfas\nEscolha a opção: ").upper()
                            if c105=="A":
                                c106=input("A.Plantas com estípulas, às vezes transformadas em glândulas\nB.Plantas sem estípulas\nEscolha a opção: ").upper()
                                if c106=="A":
                                    c107=input("A.Folhas compostas\nB.Folhas Simples\nEscolha a opção: ").upper()
                                    if c107=="A":
                                        return "Família Fabaceae(Leguminosae)"
                                    elif c107=="B":
                                        return "Família Violaceae"
                                elif c106=="B":
                                    c108=input("A.Estames 9-numerosos\nB.Estames 3-8\nEscolha a opção: ").upper()
                                    if c108=="A":
                                        return "Família Lythraceae"
                                    elif c108=="B":
                                        c109=input("A.Sepálas 2\nB.Sépalas 4-5\nEscolha a opção: ").upper()
                                        if c109=="A":
                                            return "Família Papaveraceae"
                                        elif c109=="B":
                                            c110=input("A.Sépalas 4\nB.Sépalas 5\nEscolha a opção: ").upper()
                                            if c110=="A":
                                                return "Família Brassicaceae(Cruciferae"
                                            elif c110=="B":
                                                return "Família Violaceae"
                            elif c105=="B":
                                c111=input("A.Gineceu unicarpelar\nB.Gineceu bi-pluricarpelar\nEscolha a opção: ").upper()
                                if c111=="A":
                                    c112=input("A.Corola com prefloração valvar\nB.Corola com prefloração imbricada\nEscolha a opção: ").upper()
                                    if c112=="A":
                                        return "Família Fabaceae"
                                    elif c112=="B":
                                        c113=input("A.Folhas compostas\nB.Folhas simples\nEscolha a opção: ").upper()
                                        if c113=="A":
                                            return "Família Fabaceae(Leguminosae)"
                                        elif c113=="B":
                                            return "Família Rosaceae"
                                elif c111=="B":
                                    c114=input("A.Flores com androginóforo\nB.Flores sem androginóforo\nEscolha a opção: ").upper()
                                    if c114=="A":
                                        c115=input("A.Gineceu unicarpelar\nB.Gineceu tricarpelar\nEscolha a opção: ").upper()
                                        if c115=="A":
                                            return "Família Malvaceae"
                                        elif c115=="B":
                                            return "Família Passifloraceae"
                                    elif c114=="B":
                                        c116=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção: ").upper()
                                        if c116=="A":
                                            c117=input("A.Estames 1-5\nB.Estames 6-numerosos\nEscolha a opção: ").upper()
                                            if c117=="A":
                                                c118=input("A.Flores períginas\nB.Flores hipóginas\nEscolha a opção: ").upper()
                                                if c118=="A":
                                                    return "Família Chrysobalanaceae"
                                                elif c118=="B":
                                                    c119=input("A.Óvulos com placentação parietal\nB.Óvulos com placentação central-livre, ereta ou pêndula\nEscolha a opção: ").upper()
                                                    if c119=="A":
                                                        c120=input("A.Estilete único; brácteas sem nectários extraflorais\nB.Estiletes livres entre si; brácteas geralmente com um par de nectários extraflorais na base\nEscolha a opção: ").upper()
                                                        if c120=="A":
                                                            return "Família Violaceae"
                                                        elif c120=="B":
                                                            return "Família Turneraceae"
                                                    if c119=="B":
                                                        c121=input("A.Folhas opostas\nB.Folhas alternas\nEscolha a opção: ").upper()
                                                        if c121=="A":
                                                            return "Família Caryophyllaceae"
                                                        elif c121=="B":
                                                            return "Família Malvaceae"
                                            elif c117=="B":
                                                c122=input("A.Folhas opostas\nB.Folhas alternas\nEscolha a opção: ").upper()
                                                if c122=="A":
                                                    return "Família Caryophyllaceae"
                                                elif c122=="B":
                                                    c123=input("A.Estames 10\nB.Estames numerosos\nEscolha a opção: ").upper()
                                                    if c123=="A":
                                                        return "Família Caricaceae"
                                                    if c123=="B":
                                                        c124=input("A.Cálice com prefloração valvar\nB.Cálice com prefloração imbricada\nEscolha a opção: ").upper()
                                                        if c124=="A":
                                                            return "Família Malvaceae"
                                                        if c124=="B":
                                                            return "Família Bixaceae"
                                        elif c116=="B":
                                            c125=input("A.Plantas lenhosas\nB.Plantas herbáceas\nEscolha a opção: ").upper()
                                            if c125=="A":
                                                return "Família Caricaceae"
                                            elif c125=="B":
                                                c126=input("A.Estames 5\nB.Estames 6-numerosos\nEscolha a opção: ").upper()
                                                if c126=="A":
                                                    return "Família Turneraceae"
                                                elif c126=="B":
                                                    c127=input("A.Óvulos com placentação parietal\nB.Óvulos com placentação ereta ou central-livre\nEscolha a opção: ").upper()
                                                    if c127=="A":
                                                        return "Família Papaveraceae"
                                                    elif c127=="B":
                                                        c128=input("A.Cálice 4-5mero; folhas opostas; estames 5-10\nB.Cálice (na realidade são brácteas) 2-mero; folhas alternas e opostas na mesma planta; estames 10-numerosos\nEscolha a opção: ").upper()
                                                        if c128=="A":
                                                            return "Família Caryophyllaceae"
                                                        elif c128=="A":
                                                            return "Família Portulacaceae"
                    elif c92 == "B":
                        c129 = input("A. Folhas com pontuações translúcidas\nB. Folhas sem pontuações translúcidas\nEscolha a opção: ").upper()
                        if c129 == "A":
                            c130 = input("A. Estames livres entre si\nB. Estames unidos entre si\nEscolha a opção: ").upper()
                            if c130 == "A":
                                return "Família Rutaceae"
                            elif c130 == "B":
                                c131 = input("A. Plantas com estípulas\nB. Plantas sem estípulas\nEscolha a opção: ").upper()
                                if c131 == "A":
                                    return "Família Malvaceae"
                                elif c131 == "B":
                                    c132 = input("A. Estames em número duplo ao das pétalas;plantas inermes \nB. Estames em número igual ao das pétalas ou mais que o dobro destas; plantas frequentemente com espinhos\nEscolha a opção: ").upper()
                                    if c132 == "A":
                                        return "Família Meliaceae"
                                    elif c132 == "B":
                                        return "Família Rutaceae"
                        elif c129 == "B":
                            c133 = input("A. Estames unidos entre si, formando um único ou diversos feixes\nB. Estames livres entre si ou apenas 1\nEscolha a opção: ").upper()
                            if c133 == "A":
                                c134 = input("A. Plantas com estípulas\nB. Plantas sem estípulas\nEscolha a opção: ").upper()
                                if c134 == "A":
                                    c135 = input("A. Cálice com prefloração valvar\nB. Cálice muito reduzido ou com prefloração imbricada\nEscolha a opção: ").upper()
                                    if c135 == "A":
                                        return "Família Malvaceae"
                                    elif c135 == "B":
                                        c136 = input("A. Estilete único\nB. Estiletes livres entre si\nEscolha a opção: ").upper()
                                        if c136 == "A":
                                            return "Família Geraniaceae"
                                        elif c136 == "B":
                                            return "Família Oxalidaceae"
                                elif c134 == "B":
                                    c137 = input("A. Folhas simples\nB. Folhas compostas\nEscolha a opção: ").upper()
                                    if c137 == "A":
                                        c138 = input("A. Plantas com látex\nB. Plantas sem látex\nEscolha a opção: ").upper()
                                        if c138 == "A":
                                            return "Família Clusiaceae(Guttiferae)"
                                        elif c138 == "B":
                                            return "Família Balsaminaceae"
                                    elif c137 == "B":
                                        c139 = input("A. Estiletes livres entre si\nB. Estilete único\nEscolha a opção: ").upper()
                                        if c139 == "A":
                                            return "Família Oxalidaceae"
                                        elif c139 == "B":
                                            c140 = input("A. Trepadeiras\nB. Arbustos ou árvores\nEscolha a opção: ").upper()
                                            if c140 == "A":
                                                return "Família Sapindaceae"
                                            elif c140 == "B":
                                                return "Família Meliaceae"
                            elif c133 == "B":
                                c141 = input("A. Folhas compostas\nB. Folhas simples ou compostas unifoliadas\nEscolha a opção: ").upper()
                                if c141 == "A":
                                    c142 = input("A. Gineceu 1-4-carpelar\nB. Gineceu 5-pluricarpelar\nEscolha a opção: ").upper()
                                    if c142 == "A":
                                        c143 = input("A. Lóculos do ovário com um único óvulo\nB. Lóculos do ovário com dois a muitos óvulos\nEscolha a opção: ").upper()
                                        if c143 == "A":
                                            c144 = input("A. Estames 2-7\nB. Estames 8-12\nEscolha a opção: ").upper()
                                            if c144 == "A":
                                                return "Família Sapindaceae"
                                            elif c144 == "B":
                                                c145 = input("A. Prefloração da corola valvar\nB. Prefloração da corola imbricada\nEscolha a opção: ").upper()
                                                if c145 == "A":
                                                    return "Família Anacardiaceae"
                                                elif c145 == "B":
                                                    return "Família Sapindaceae"
                                        elif c143 == "B":
                                            c146 = input("A. Estames 2-5\nB. Estames 6-12\nEscolha a opção: ").upper()
                                            if c146 == "A":
                                                return "Família Vitaceae"
                                            elif c146 == "B":
                                                return "Família Sapindaceae"
                                    elif c142 == "B":
                                        c147 = input("A. Lóculos do ovário com um único óvulo\nB. Lóculos do ovário com dois a muitos óvulos\nEscolha a opção: ").upper()
                                        if c147 == "A":
                                            return "Família Anacardiaceae"
                                        elif c147 == "B":
                                            c148 = input("A. Folhas digitadas\nB. Folhas binadas ou bipinadas\nEscolha a opção: ").upper()
                                            if c148 == "A":
                                                return "Família Caricaceae"
                                            elif c148 == "B":
                                                return "Família Meliaceae"
                                elif c141 == "B":
                                    c149 = input("A. Flores zigomorfas\nB. Flores actinomorfas\nEscolha a opção: ").upper()
                                    if c149 == "A":
                                        c150 = input("A. Estames 2-8\nB. Estames 10-numerosos\nEscolha a opção: ").upper()
                                        if c150 == "A":
                                            c151 = input("A. Folhas opostas ou verticiladas\nB. Folhas alternas\nEscolha a opção: ").upper()
                                            if c151 == "A":
                                                c152 = input("A. Lóculos do ovário com dois ou mais óvulos\nB. Lóculos do ovário com um único óvulo\nEscolha a opção: ").upper()
                                                if c152 == "A":
                                                    return "Família Lythraceae"
                                                elif c152 == "B":
                                                    return "Família Malpighiaceae"
                                            elif c151 == "B":
                                                c153 = input("A. Flores calcaradas\nB. Flores não calcaradas\nEscolha a opção: ").upper()
                                                if c153 == "A":
                                                    return "Família Tropeolaceae"
                                                elif c153 == "B":
                                                    c154 = input("A. Flores hexâmeras\nB. Flores 4-5-meras\nEscolha a opção: ").upper()
                                                    if c154 == "A":
                                                        return "Família Lytrhaceae"
                                                    elif c154 == "B":
                                                        return "Família Sapindaceae"
                                        elif c150 == "B":
                                            c155 = input("A. Gineceu tetra-pentacarpelar\nB. Gineceu bi-tricarpelar\nEscolha a opção: ").upper()
                                            if c155 == "A":
                                                return "Família Geraniaceae"
                                            elif c155 == "B":
                                                c156 = input("A. Lóculos do ovário com um único óvulo; cálice geralmente com um par de glândulas nectaríferas(elaióforos)\nB. Lóculos do ovário com dois a muitos óvulos; cálice sem glândulas\nEscolha a opção: ").upper()
                                                if c156 == "A":
                                                    return "Família Malpighiaceae"
                                                elif c156 == "B":
                                                    return "Família Lythraceae"
                                    elif c149 == "B":
                                        c157=input("A.Plantas aquáticas\nB.Plantas terrestres\nEscolha a opção: ").upper()
                                        if c157=="A":
                                            return "Família Nymphaeaceae"
                                        elif c157=="B":
                                            c158=input("A.Folhas opostas ou verticiladas\nB.Folhas alternas\nEscolha a opção: ").upper()
                                            if c158=="A":
                                                c159=input("A.Plantas com látex\nB.Plantas sem látex\nEscolha a opção: ").upper()
                                                if c159=="A":
                                                    c160=input("A.Estigma séssil ou subséssil\nB.Estilete conspícuo\nEscolha a opção: ").upper()
                                                    if c160=="A":
                                                        return "Família Clusiaceae(Guttiferae)"
                                                    elif c160=="B":
                                                        c161=input("A.Plantas com estípulas\nB.Plantas sem estípulas\nEscolha a opção: ").upper()
                                                        if c161=="A":
                                                            return "Família Euphorbiaceae"
                                                        elif c161=="B":
                                                            return "Família Clusiaceae(Guttiferae)"
                                                elif c159=="B":
                                                    c162=input("A.Estames 1-5\nB.Estames 6-numerosos\nEscolha a opção: ").upper()
                                                    if c162=="A":
                                                        c163=input("A.Sépalas com um par de nectários extraflorais (elaióforos) em sua face externa\nB.Sépalas sem nectários extraflorais em sua face externa\nEscolha a opção: ").upper()
                                                        if c163=="A":
                                                            return "Família Malpighiaceae"
                                                        elif c163=="B":
                                                            return "Família Lythraceae"
                                                    elif c162=="B":
                                                        c164=input("A.Sépalas com um par de nectários extraflorais (elaióforos) em sua face externa\nB.Sépalas sem nectários extraflorais em sua face externa\nEscolha a opção: ").upper()
                                                        if c164=="A":
                                                            return "Família Malpighiaceae"
                                                        elif c164=="B":
                                                            c165=input("A.Arbustos ou árvores\nB.Ervas ou subarbustos\nEscolha a opção: ").upper()
                                                            if c165=="A":
                                                                c166=input("A.Folhas geralmente curvinérveas; anteras falciformes\nB.Folhas uninérveas, palminérveas ou peninérveas; anteras não falciformes\nEscolha a opção: ").upper()
                                                                if c166=="A":
                                                                    return "Família Melastomataceae"
                                                                elif c166=="B":
                                                                    return "Família Lythraceae"
                                                            elif c165=="B":
                                                                c167=input("A.Folhas geralmente curvinérveas; anteras falciformes\nB.Folhas uninérveas, palminérveas ou peninérveas; anteras não falciformes\nEscolha a opção: ").upper()
                                                                if c167=="A":
                                                                    return "Família Melastomataceae"
                                                                elif c167=="B":
                                                                    return "Família Lythraceae"
                                            elif c158=="B":
                                                c168=input("A.Plantas sem estípulas\nB.Plantas com estípulas\nEscolha a opção: ").upper()
                                                if c168=="A":
                                                    c169=input("A.Lóculos do ovário 1-2-ovulados\nB.Lóculos do ovário 3-pluriovulados\nEscolha a opção: ").upper()
                                                    if c169=="A":
                                                        c170=input("A.Estames 10-numerosos\nB.Estames 2-9\nEscolha a opção: ").upper()
                                                        if c170=="A":
                                                            return "Família Annonaceae"
                                                        elif c170=="B":
                                                            c171=input("A.Ervas\nB.Plantas lenhosas\nEscolha a opção: ").upper()
                                                            if c171=="A":
                                                                return "Família Linaceae"
                                                            elif c171=="B":
                                                                return "Família Rutaceae"
                                                    elif c169=="B":
                                                        c172=input("A.Ovário 4-7-locular\nB.Ovário bi-trilocular\nEscolha a opção: ").upper()
                                                        if c172=="A":
                                                            c173=input("A.Estames 5-10\nB.Estames numerosos\nEscolha a opção: ").upper()
                                                            if c173=="A":
                                                                return "Família Caricaceae"
                                                            elif c173=="B":
                                                                return "Família Lythraceae"
                                                        elif c172=="B":
                                                            c174=input("A.Estames tetradínamos\nB.Estames não tetradínamos\nEscolha a opção: ").upper()
                                                            if c174=="A":
                                                                return "Família Brassicaceae(Cruciferae)\nObs: Possui falso septo, sendo seu ovário unilocular"
                                                            elif c174=="B":
                                                                return "Família Clusiaceae(Guttiferae)"
                                                elif c168=="B":
                                                    c175=input("A.Estames 2-8\nB.Estames 10-numerosos\nEscolha a opção: ").upper()
                                                    if c175=="A":
                                                        c176=input("A.Gineceu pentacarpelar\nB.Gineceu 2-4 carpelar\nEscolha a opção: ").upper()
                                                        if c176=="A":
                                                            return "Família Malvaceae"
                                                        elif c176=="B":
                                                            c177=input("A.Flores bissexuadas\nB.Flores unissexuadas\nEscolha a opção: ").upper()
                                                            if c177=="A":
                                                                c178=input("A.Lianas\nnB.Plantas eretas\nEscolha a opção: ").upper()
                                                                if c178=="A":
                                                                    return "Família Vitaceae"
                                                                elif c178=="B":
                                                                    c179=input("A.Flores sem disco nectarífero\nB.Flores com disco nectarífero\nEscolha a opção: ").upper()
                                                                    if c179=="A":
                                                                        return "Família Malvaceae"
                                                                    elif c179=="B":
                                                                        c180=input("A.Lóculos do ovário uniovulados\nB.Lóculos do ovário pluriovulados\nEscolha a opção: ").upper()
                                                                        if c180=="A":
                                                                            return "Família Rhamnaceae"
                                                                        elif c180=="B":
                                                                            return "Família Brassicaceae(Cruciferae)"
                                                            elif c177=="B":
                                                                c181=input("A.Lóculos do ovário com dois a muitos óvulos\nB.Lóculos do ovário com um único óvulo\nEscolha a opção: ").upper()
                                                                if c181=="A":
                                                                    return "Família Vitaceae"
                                                                elif c181=="B":
                                                                    return "Família Euphorbiaceae"
                                                    elif c175=="B":
                                                        c182=input("A.Lóculos do ovário 1-2-ovulados\nB.Lóculos do ovário pluriovulados\nEscolha a opção: ").upper()
                                                        if c182=="A":
                                                            c183=input("A.Flores solitárias ou disposta em fascículos\nB.Flores dispostas em inflorescências de outros tipos\nEscolha a opção: ").upper()
                                                            if c183=="A":
                                                                c184=input("A.Plantas com estípulas intrapeciolares mais persistentes do que as folhas, formando ramentas\nB.Plantas com ou sem estípulas, não formando ramentas\nEscolha a opção: ").upper()
                                                                if c184=="A":
                                                                    return "Família Erythroxylaceae"
                                                                elif c184=="B":
                                                                    return "Família Geraniaceae"
                                                            elif c183=="B":
                                                                c185=input("A.Flores unissexuadas\nB.Flores bissexuadas\nEscolha a opção: ").upper()
                                                                if c185=="A":
                                                                    c186=input("A.Lóculos do ovário com um único óvulo\nB.Lóculos do ovário biovulados\nEscolha a opção: ").upper()
                                                                    if c186=="A":
                                                                        return "Família Euphorbiaceae"
                                                                    elif c186=="B":
                                                                        return "Família Malvaceae"
                                                                elif c185=="B":
                                                                    c187=input("A.Cálice com prefloração valvar\nB.Cálice com prefloração imbricada\nEscolha a opção: ").upper()
                                                                    if c187=="A":
                                                                        return "Família Malvaceae"
                                                                    elif c187=="B":
                                                                        return "Famíia Geraniaceae"
                                                        elif c182=="B":
                                                            c188=input("A.Anteras rimosas\nB.Anteras poricidas\nEscolha a opção: ").upper()
                                                            if c188=="A":
                                                                return "Família Muntingiaceae"
                                                            elif c188=="B":
                                                                return "Família Bixaceae"
                                                                
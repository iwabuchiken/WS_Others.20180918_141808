# -*- coding: utf-8 -*-

'''
pushd C:\WORKS_2\WS\WS_Others\JVEMV6\37\3_
1_.py

'''
from itertools import count

'''
    Regex
print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^ +(print )(".+" %.+\(.+\).*)$
^( +)(print )(".+" %.+\(.+\).*)$
$1$2($3)

print "[%s:%d] result => %s" % \
        (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^( +)(print )(".+" %) \\\r\n(.+)$
$1$2($3)$4$5
$1$2($3 \\\r\n$4)

print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
^( +)(print )(.+)(libs.+file\(\))(.+)
$1$2$3os.path.basename($4)$5
'''


import sys
from sympy.solvers.tests.test_constantsimp import C2

# sys.setdefaultencoding('utf8')  #=> AttributeError: module 'sys' has no attribute 'setdefaultencoding'

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs

import os
import inspect

import math as math

import re

###############################################
#ref article http://toyokeizai.net/articles/-/202462
# text = '''
# ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。
# 「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」
# 「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」
# ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。
# 「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」
# 日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。
# 夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。
# 月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。
# 「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」
# 「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」
# お茶をすすりながらフサエさんはため息混じりに語った。  
# 定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。
# 日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。
# 現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。
# 国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。
# 理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。
# このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。
# 「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。自営業で国民年金にしか加入していなかった人や、フサエさんのように長年働き続けていても低賃金だったために、支払われる年金額が少なかった人もいる。
# そんな”隠れ貧困層”を直撃するのは、2016年末の臨時国会で成立した「年金カット法案」だ。現在導入されている「マクロ経済スライド」は、デフレ下では発動されないため、将来的な物価上昇の見通しが立たない現状では、年金支給額の抑制が厳しい。そこで、デフレ下でも年金の支給額を抑制できるように、「物価と賃金の低いほうにつねに合わせて年金を下げる」という仕組みを盛り込んだ改正国民年金法が2021年4月から実施される。
# 2016年12月下旬、厚生労働省が公表した試算によると、物価上昇率が1.2％、経済成長率が0.4％のケースでは、高齢者への年金支給額は新ルールを導入しない場合と比べて2026年度から2043年度まで0.6％減る。民進党が公表した試算では、国民年金は年間4万円、厚生年金は同14万円も減るという恐ろしい結果が出ている。今、ぎりぎりで生活している高齢者たちは、生活が立ち行かなくなるのは目に見えている。
# 一般的に会社を定年退職したあとに、健康保険組合から国保に移る。年齢とともに病院に通う人が多くなるので、高齢者の加入率が高い国保は、その分保険料を上げないと医療費を賄えない構造になっている。国保の負担増も高齢者にとってかなりの痛手だ。
# 東京都に住むシンジさん（仮名、67歳）も年金カットと国保の負担増で悲鳴を上げている高齢者の1人。現在、年金を受け取りながら運送業のアルバイトで生計を立てている。
# 「アベノミクスの影響で、株で儲かった人もいるようですが、私たちには関係ない話だね。年々、仕事が減って、最近の手取りは年100万円程度でした」（シンジさん）
# シンジさんの年金は年間約60万円。長年、自営業を営んでいたため厚生年金はない。60代で店を畳み、アルバイトをはじめた。同い年の妻は腎臓が悪く、定期的に病院に通い人工透析を受けている。ほとんど寝たきりの状態で要介護度は2番目に重い「要介護4」。排泄は自力でなんとかできても、家事は一切できないため、シンジさんが妻に代わって一切を行っている。そして、ひきこもりで働くことができない娘（30代）の3人で暮らしている。
# 妻の年金はすべて妻自身の医療費に消える。所得税と住民税は非課税に該当しても、年13万円の国民健康保険料の支払い義務はあった。
# 「兄一家と同居しているので、家賃の負担がないのが幸いですが、国保の保険料と光熱費を差し引くと手元には月10万円しか残らない。家族3人で食べていくのが精いっぱいですよ」（シンジさん）
# 東京23区の保険料は住民税を基に計算されていたが、2013年度より所得から33万円の基礎控除を差し引いた「所得」が算出のもとになった。変更後は、扶養家族や障害者・寡婦などの控除が適用されなくなり、一部の世帯では保険料が上がった。シンジさんに限らず、年収が少なく家族が多い世帯の家計を直撃した。豊島区を例にとると、年収200万円の年金受給者夫婦二人世帯では、年6万3840円から年8万5886円と、約2万2000円上がった。シンジさんも以前と比較して2万円の負担が増えた。
# 「世の中の人は『もっと働けばいいじゃない』と思うかもしれませんが、妻が病院に行くときは私が付き添い、普段も食事の世話をしなければならないので、働きたくても働けない。1カ月のうち10〜15日が限界です。それに私だって高齢者なので、現役世代のようにもっと働けといっても体がいうことを聞きませんし、これ以上は無理ですよ」
# シンジさんは自分が病気で倒れたときのことを考えると背筋が凍るというが、なすすべもない。住居は持ち家の扱いなので、基本的に生活保護の受給対象にならないからだ。
# 「首から上は元気なんだけどね」と笑うのは、埼玉県に住むスミコさん（仮名、79歳）。
# 60代でリウマチにかかり、10年前に頚椎の手術を受けた。歩行が困難で買い物を含めて家事のほとんどは夫（80歳）が行う。
# 「トイレが近くて夜中に何度も起きるのが嫌で、あまりお水を飲まなかったら去年の夏に熱中症になりかけちゃって。猛暑日が続いても電気代がもったいないから、クーラーをつけなかったのが、よくなかったのかもしれないね」
# 『介護破産 働きながら介護を続ける方法』（書影をクリックすると、アマゾンのサイトにジャンプします）
# 節約するのにはワケがある。夫との年金は2人合わせて約15万円。持ち家なので家賃はないが”老後”のために生活費を抑えて少しでも貯金に回している。
# “最後のセーフティーネット”といわれる生活保護受給の条件は、①現在手持ちのおカネがわずかな状態、②すぐに現金化が可能な資産を持っていないことなどだ。単身世帯に支給される保護費は、東京23区で月13万円程度。所持金が13万円を下回っていれば、受給の対象になる。
# また、②の現金化可能な資産については、自宅、車、保険などが対象とされている。例外もあるので詳しい情報は住む自治体の社会福祉事務所に確認をする必要があるが、一般的に持ち家は資産と見なされるので、低年金でも持ち家があると生活保護が受けられないケースが多い。前出のシンジさん一家や、スミコさん夫婦は、生活に困窮していても生活保護の対象外になる。
# 夫婦に子どもはいない。夫はまだ一度も大病を患ったことはないというが、すでに80代。いつまでもこのままの生活が続くとは思っていない。
# 「万が一、夫が私よりも先立つようなことがあったら、どうしよう……」
# スミコさんの苦悩は尽きない。
# '''

# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、していても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。"
# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。"

# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。"

text_3 = u"1カ月のうち10〜15日が限界です。それに私だって高齢者なので、現役世代のようにもっと働けといっても体がいうことを聞きませんし、これ以上は無理ですよ」シンジさんは自分が病気で倒れたときのことを考えると背筋が凍るというが、なすすべもない。住居は持ち家の扱いなので、基本的に生活保護の受給対象にならないからだ。「首から上は元気なんだけどね」と笑うのは、埼玉県に住むスミコさん（仮名、79歳）。60代でリウマチにかかり、10年前に頚椎の手術を受けた。歩行が困難で買い物を含めて家事のほとんどは夫（80歳）が行う。「トイレが近くて夜中に何度も起きるのが嫌で、あまりお水を飲まなかったら去年の夏に熱中症になりかけちゃって。猛暑日が続いても電気代がもったいないから、クーラーをつけなかったのが、よくなかったのかもしれないね」『介護破産 働きながら介護を続ける方法』（書影をクリックすると、アマゾンのサイトにジャンプします）節約するのにはワケがある。夫との年金は2人合わせて約15万円。持ち家なので家賃はないが”老後”のために生活費を抑えて少しでも貯金に回している。“最後のセーフティーネット”といわれる生活保護受給の条件は、①現在手持ちのおカネがわずかな状態、②すぐに現金化が可能な資産を持っていないことなどだ。単身世帯に支給される保護費は、東京23区で月13万円程度。所持金が13万円を下回っていれば、受給の対象になる。また、②の現金化可能な資産については、自宅、車、保険などが対象とされている。例外もあるので詳しい情報は住む自治体の社会福祉事務所に確認をする必要があるが、一般的に持ち家は資産と見なされるので、低年金でも持ち家があると生活保護が受けられないケースが多い。前出のシンジさん一家や、スミコさん夫婦は、生活に困窮していても生活保護の対象外になる。夫婦に子どもはいない。夫はまだ一度も大病を患ったことはないというが、すでに80代。いつまでもこのままの生活が続くとは思っていない。「万が一、夫が私よりも先立つようなことがあったら、どうしよう……」スミコさんの苦悩は尽きない。"
text_2 = u"「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。自営業で国民年金にしか加入していなかった人や、フサエさんのように長年働き続けていても低賃金だったために、支払われる年金額が少なかった人もいる。そんな”隠れ貧困層”を直撃するのは、2016年末の臨時国会で成立した「年金カット法案」だ。現在導入されている「マクロ経済スライド」は、デフレ下では発動されないため、将来的な物価上昇の見通しが立たない現状では、年金支給額の抑制が厳しい。そこで、デフレ下でも年金の支給額を抑制できるように、「物価と賃金の低いほうにつねに合わせて年金を下げる」という仕組みを盛り込んだ改正国民年金法が2021年4月から実施される。2016年12月下旬、厚生労働省が公表した試算によると、物価上昇率が1.2％、経済成長率が0.4％のケースでは、高齢者への年金支給額は新ルールを導入しない場合と比べて2026年度から2043年度まで0.6％減る。民進党が公表した試算では、国民年金は年間4万円、厚生年金は同14万円も減るという恐ろしい結果が出ている。今、ぎりぎりで生活している高齢者たちは、生活が立ち行かなくなるのは目に見えている。一般的に会社を定年退職したあとに、健康保険組合から国保に移る。年齢とともに病院に通う人が多くなるので、高齢者の加入率が高い国保は、その分保険料を上げないと医療費を賄えない構造になっている。国保の負担増も高齢者にとってかなりの痛手だ。東京都に住むシンジさん（仮名、67歳）も年金カットと国保の負担増で悲鳴を上げている高齢者の1人。現在、年金を受け取りながら運送業のアルバイトで生計を立てている。「アベノミクスの影響で、株で儲かった人もいるようですが、私たちには関係ない話だね。年々、仕事が減って、最近の手取りは年100万円程度でした」（シンジさん）シンジさんの年金は年間約60万円。長年、自営業を営んでいたため厚生年金はない。60代で店を畳み、アルバイトをはじめた。同い年の妻は腎臓が悪く、定期的に病院に通い人工透析を受けている。ほとんど寝たきりの状態で要介護度は2番目に重い「要介護4」。排泄は自力でなんとかできても、家事は一切できないため、シンジさんが妻に代わって一切を行っている。そして、ひきこもりで働くことができない娘（30代）の3人で暮らしている。妻の年金はすべて妻自身の医療費に消える。所得税と住民税は非課税に該当しても、年13万円の国民健康保険料の支払い義務はあった。「兄一家と同居しているので、家賃の負担がないのが幸いですが、国保の保険料と光熱費を差し引くと手元には月10万円しか残らない。家族3人で食べていくのが精いっぱいですよ」（シンジさん）東京23区の保険料は住民税を基に計算されていたが、2013年度より所得から33万円の基礎控除を差し引いた「所得」が算出のもとになった。変更後は、扶養家族や障害者・寡婦などの控除が適用されなくなり、一部の世帯では保険料が上がった。シンジさんに限らず、年収が少なく家族が多い世帯の家計を直撃した。豊島区を例にとると、年収200万円の年金受給者夫婦二人世帯では、年6万3840円から年8万5886円と、約2万2000円上がった。シンジさんも以前と比較して2万円の負担が増えた。「世の中の人は『もっと働けばいいじゃない』と思うかもしれませんが、妻が病院に行くときは私が付き添い、普段も食事の世話をしなければならないので、働きたくても働けない。"
# text_2 = "「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。自営業で国民年金にしか加入していなかった人や、フサエさんのように長年働き続けていても低賃金だったために、支払われる年金額が少なかった人もいる。そんな”隠れ貧困層”を直撃するのは、2016年末の臨時国会で成立した「年金カット法案」だ。現在導入されている「マクロ経済スライド」は、デフレ下では発動されないため、将来的な物価上昇の見通しが立たない現状では、年金支給額の抑制が厳しい。そこで、デフレ下でも年金の支給額を抑制できるように、「物価と賃金の低いほうにつねに合わせて年金を下げる」という仕組みを盛り込んだ改正国民年金法が2021年4月から実施される。2016年12月下旬、厚生労働省が公表した試算によると、物価上昇率が1.2％、経済成長率が0.4％のケースでは、高齢者への年金支給額は新ルールを導入しない場合と比べて2026年度から2043年度まで0.6％減る。民進党が公表した試算では、国民年金は年間4万円、厚生年金は同14万円も減るという恐ろしい結果が出ている。今、ぎりぎりで生活している高齢者たちは、生活が立ち行かなくなるのは目に見えている。一般的に会社を定年退職したあとに、健康保険組合から国保に移る。年齢とともに病院に通う人が多くなるので、高齢者の加入率が高い国保は、その分保険料を上げないと医療費を賄えない構造になっている。国保の負担増も高齢者にとってかなりの痛手だ。東京都に住むシンジさん（仮名、67歳）も年金カットと国保の負担増で悲鳴を上げている高齢者の1人。現在、年金を受け取りながら運送業のアルバイトで生計を立てている。「アベノミクスの影響で、株で儲かった人もいるようですが、私たちには関係ない話だね。年々、仕事が減って、最近の手取りは年100万円程度でした」（シンジさん）シンジさんの年金は年間約60万円。長年、自営業を営んでいたため厚生年金はない。60代で店を畳み、アルバイトをはじめた。"
# text_2 = "「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。"
text_1 = u"ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。"
# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。"
# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。"    #=> works
# text = "ある都営住宅の一室。一人暮らしの高齢者5人が集い、こたつを囲んでお茶をすすっていた。今日の天気からはじまり、孫のこと、病気のこと、話題は尽きない。ニュースで取り上げられている「年金」について1人が切り出した。「これ以上年金を減らされたら、私たちの生活はどうなっちゃうの？」「テレビや新聞で年金の話題が取り上げられても、内容が難しくてさっぱりわからないよ」ただ、1つだけ理解している点は、受け取る年金は将来にわたって減らされるということ。長生きすればするほど、生活が苦しくなる。笑い飛ばしていても、目つきは真剣だ。「消費税が上がってから、何を買っても高くつくので、食べ物や生活必需品以外は本当に買わなくなりましたね。洋服も以前は、お店の前を通ったら『あら、これいいわね』と、毎シーズン1つは新しいものを買っていましたが、新調しないでなるべく着まわししなくては。外出しても何も買わないでまっすぐ家に帰るようにしています」日本年金機構から毎年送られてくる「ハガキ」を片手に深いため息をつくのは、都営住宅に住むフサエさん（仮名、77歳）。定年退職後、年金をもらいながら趣味を謳歌する……そんな悠々自適な生活を思い浮かべながら、現役時代は必死に働き続けた。ところが、いざ年金を受け取ってみると、あまりの少なさにショックを受けた。夫が15年前に他界してからは一人暮らし。嫁いだ2人の娘たちが時折、フサエさんの様子をうかがいに訪ねてくる。定年まで企業の食堂などで働いたので、夫の扶養には入らず厚生年金に加入していた。現在、月に受け取る年金額は厚生年金と国民年金などを合わせて約13万円。「長年働いた割には少ない」というのが実感だった。女性は男性よりも賃金が低いため、支払う年金保険料が少ないからだ。月々の生活で出費のウェートを占めるのは食費と光熱費、そして医療・介護費。フサエさんは糖尿病の持病があり、入退院を繰り返している。要介護度は7段階でいちばん軽い要支援1。週に2回、デイサービスに通う。3年前に転倒して足を骨折したときの後遺症でリハビリを行うためだ。歩行が困難になりシルバーカーを押しながらやっとの思いで歩いている。このほかに、定期的に内科と整形外科に通う。医療費は薬代を含めて1割自己負担で月5000円程度。介護保険のサービス利用料も同様に1割負担で約5000円。そして、ガスストーブをつけて暖を取る冬場の光熱費は1万4000円にもなる。「年金生活に入ってからは家賃の減免申請をしたので1万1600円。光熱費、医療費、介護の費用が何かとかかるので、貯金を切り崩しながら生活しています。生活はいっぱい、いっぱいですよ。これから先、今まで以上に病院や介護のおカネが必要になったらどうしようと不安になります」「娘たち？ 孫の教育費やら何やら、娘たちにも生活があるのでアテにできませんね。年金で生活できなくなったら生活保護に頼るしかないわね」お茶をすすりながらフサエさんはため息混じりに語った。  定年まで働いたのにもかかわらず、余裕がない生活を余儀なくされているのは、もらえる年金が少ないから。ひとたび病気や介護をきっかけに費用の負担が増えれば生活が成り立たなくなる……。介護破産“予備軍“の1つはフサエさんたちのような、年金受給額が低い高齢者たちだ。日本の公的年金制度（厚生年金と国民年金）は、現役世代の保険料負担で、高齢者世代を支える「世代間扶養」の考え方を基本として運営されている。しかし、少子高齢化が進むなかで、現役世代が納付する保険料のみでは年金給付を賄いきれなくなっている。現役世代6713万人の保険料収入は37兆6000億円。これに対して、年金受給の高齢者は3991万人で給付総額は53兆4000億円（いずれも2014年）。保険料収入よりも給付額が上回っている状態だ。給付額の不足分は、国庫（税金）から補塡し、さらに保険料の一部を「年金積立金」として保有して、一部を運用しながら切り崩している。国は年金制度を維持するために、制度改正を何度も行っている。2004年に、自民・公明連立政権下で「年金100年安心プラン」と題し、今後100年間、年金の受取額は現役時代の収入に対して最低50％を保証するために、年金制度の改革が行われた。その1つが、「マクロ経済スライド」だ。理解を深めるために、ここで年金について、もう一度、おさらいしよう。そもそも、年金額は物価や賃金の変動に応じて、毎年改定されることになっている。物価が上昇すれば年金額も上がり、下降すれば下がる「物価スライド」が導入されている。ところが、「高齢者の生活の配慮」を理由に、2000年度から、当時の自公政権が物価スライドを凍結させた。物価の下降に合わせて年金額を減額すべきところを据え置いたのだ。このため、本来もらうべき年金額よりも多くもらっていた受給者は適正額に戻すために、2013年10月から1％、翌14年4月からさらに1％減額され、2015年4月にも0.5％下げられた。「もらいすぎ」が解消されれば、物価や賃金が上昇すると、その分年金額も上がることになる。その伸びを抑える役割を果たすのが、「マクロ経済スライド」だ。2015年度、厚生年金を受け取る夫婦二人世帯のモデル世帯は、前年度より4453円プラスの月22万3519円もらえるはずだった。ところが実際の受給額は月22万1507円。マクロ経済スライドにより、2012円減った。しかし、この額はあくまでもモデルであり、年金受給者3991万人のうち、約4分の1が生活保護の基準以下で生活する”隠れ貧困層”といわれる。自営業で国民年金にしか加入していなかった人や、フサエさんのように長年働き続けていても低賃金だったために、支払われる年金額が少なかった人もいる。そんな”隠れ貧困層”を直撃するのは、2016年末の臨時国会で成立した「年金カット法案」だ。現在導入されている「マクロ経済スライド」は、デフレ下では発動されないため、将来的な物価上昇の見通しが立たない現状では、年金支給額の抑制が厳しい。そこで、デフレ下でも年金の支給額を抑制できるように、「物価と賃金の低いほうにつねに合わせて年金を下げる」という仕組みを盛り込んだ改正国民年金法が2021年4月から実施される。2016年12月下旬、厚生労働省が公表した試算によると、物価上昇率が1.2％、経済成長率が0.4％のケースでは、高齢者への年金支給額は新ルールを導入しない場合と比べて2026年度から2043年度まで0.6％減る。民進党が公表した試算では、国民年金は年間4万円、厚生年金は同14万円も減るという恐ろしい結果が出ている。今、ぎりぎりで生活している高齢者たちは、生活が立ち行かなくなるのは目に見えている。一般的に会社を定年退職したあとに、健康保険組合から国保に移る。年齢とともに病院に通う人が多くなるので、高齢者の加入率が高い国保は、その分保険料を上げないと医療費を賄えない構造になっている。国保の負担増も高齢者にとってかなりの痛手だ。東京都に住むシンジさん（仮名、67歳）も年金カットと国保の負担増で悲鳴を上げている高齢者の1人。現在、年金を受け取りながら運送業のアルバイトで生計を立てている。「アベノミクスの影響で、株で儲かった人もいるようですが、私たちには関係ない話だね。年々、仕事が減って、最近の手取りは年100万円程度でした」（シンジさん）シンジさんの年金は年間約60万円。長年、自営業を営んでいたため厚生年金はない。60代で店を畳み、アルバイトをはじめた。同い年の妻は腎臓が悪く、定期的に病院に通い人工透析を受けている。ほとんど寝たきりの状態で要介護度は2番目に重い「要介護4」。排泄は自力でなんとかできても、家事は一切できないため、シンジさんが妻に代わって一切を行っている。そして、ひきこもりで働くことができない娘（30代）の3人で暮らしている。妻の年金はすべて妻自身の医療費に消える。所得税と住民税は非課税に該当しても、年13万円の国民健康保険料の支払い義務はあった。「兄一家と同居しているので、家賃の負担がないのが幸いですが、国保の保険料と光熱費を差し引くと手元には月10万円しか残らない。家族3人で食べていくのが精いっぱいですよ」（シンジさん）東京23区の保険料は住民税を基に計算されていたが、2013年度より所得から33万円の基礎控除を差し引いた「所得」が算出のもとになった。変更後は、扶養家族や障害者・寡婦などの控除が適用されなくなり、一部の世帯では保険料が上がった。シンジさんに限らず、年収が少なく家族が多い世帯の家計を直撃した。豊島区を例にとると、年収200万円の年金受給者夫婦二人世帯では、年6万3840円から年8万5886円と、約2万2000円上がった。シンジさんも以前と比較して2万円の負担が増えた。「世の中の人は『もっと働けばいいじゃない』と思うかもしれませんが、妻が病院に行くときは私が付き添い、普段も食事の世話をしなければならないので、働きたくても働けない。1カ月のうち10〜15日が限界です。それに私だって高齢者なので、現役世代のようにもっと働けといっても体がいうことを聞きませんし、これ以上は無理ですよ」シンジさんは自分が病気で倒れたときのことを考えると背筋が凍るというが、なすすべもない。住居は持ち家の扱いなので、基本的に生活保護の受給対象にならないからだ。「首から上は元気なんだけどね」と笑うのは、埼玉県に住むスミコさん（仮名、79歳）。60代でリウマチにかかり、10年前に頚椎の手術を受けた。歩行が困難で買い物を含めて家事のほとんどは夫（80歳）が行う。「トイレが近くて夜中に何度も起きるのが嫌で、あまりお水を飲まなかったら去年の夏に熱中症になりかけちゃって。猛暑日が続いても電気代がもったいないから、クーラーをつけなかったのが、よくなかったのかもしれないね」『介護破産 働きながら介護を続ける方法』（書影をクリックすると、アマゾンのサイトにジャンプします）節約するのにはワケがある。夫との年金は2人合わせて約15万円。持ち家なので家賃はないが”老後”のために生活費を抑えて少しでも貯金に回している。“最後のセーフティーネット”といわれる生活保護受給の条件は、①現在手持ちのおカネがわずかな状態、②すぐに現金化が可能な資産を持っていないことなどだ。単身世帯に支給される保護費は、東京23区で月13万円程度。所持金が13万円を下回っていれば、受給の対象になる。また、②の現金化可能な資産については、自宅、車、保険などが対象とされている。例外もあるので詳しい情報は住む自治体の社会福祉事務所に確認をする必要があるが、一般的に持ち家は資産と見なされるので、低年金でも持ち家があると生活保護が受けられないケースが多い。前出のシンジさん一家や、スミコさん夫婦は、生活に困窮していても生活保護の対象外になる。夫婦に子どもはいない。夫はまだ一度も大病を患ったことはないというが、すでに80代。いつまでもこのままの生活が続くとは思っていない。「万が一、夫が私よりも先立つようなことがあったら、どうしよう……」スミコさんの苦悩は尽きない。"

text = text_1 + text_2 + text_3

def exec_prog(): #
     
    '''###################
        prep : text        
    ###################'''
#     fin = open("article.txt", "r", encoding='CP932')
# #     fin = open("article.txt", "r", encoding='shift-jis')
# #     fin = open("article.txt", "r", encoding='UTF-8')
# #     fin = open("article.txt", "r")
#      
#     text = fin.read()
#      
#     fin.close()
#     
#     print(text)
    
    # regex
    #ref https://stackoverflow.com/questions/4995892/python-split-string-on-regex
    p = re.compile('[。、]')
    
    ary = p.split(text)
#     ary = text.split("。")
    
    # ary of num
    aryOf_TokenLen = []
    
    for item in ary :
        
        lenOf_Item = len(item)
        
#         print ("len => %d [%s]" % (lenOf_Item, item))
        
        if lenOf_Item > 5 : aryOf_TokenLen.append(lenOf_Item)
    
#         aryOf_TokenLen.append(lenOf_Item)
    
    ### report
    print ("[%s:%d] average => %.3f" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), 
            #ref sum https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
            sum(aryOf_TokenLen) / len(aryOf_TokenLen)))
#             aryOf_TokenLen.sum() / len(aryOf_TokenLen)))

    print(aryOf_TokenLen)
    
    '''###################
        write to file        
    ###################'''
    fname = "data/report.%s.txt" % (libs.get_TimeLabel_Now())
    f = open(fname, "w")
    
    #ref sort https://www.tutorialspoint.com/python/list_sort.htm
    aryOf_TokenLen__Sorted = aryOf_TokenLen.sort()
    
    # get max
    len_Max = -1
    

    for item in aryOf_TokenLen :
        
        # get max
        if len_Max < item : len_Max = item

        
        for i in range(item) :
            
            f.write("*")
        
        # return
        f.write("\n")

    f.close()
    
    print ("[%s:%d] file => closed : %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), fname))
        
    print ("[%s:%d] max len => %d" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), len_Max))
    
    
    '''###################
        Out : histogram        
    ###################'''
    aryOf_Histogram = {}
    
    #test
    print()
    print(range(len_Max))
    
    # init
    for i in range(len_Max + 1) : aryOf_Histogram[i] = 0
#     for i in range(len_Max) : aryOf_Histogram[i] = 0
    
    for item in aryOf_TokenLen :
          
        aryOf_Histogram[item] += 1
    
    ### report
    print()
    print(aryOf_Histogram)
    
    ### write to file
    fname = "data/report.histogram.%s.txt" % (libs.get_TimeLabel_Now())
    
    f = open(fname, "w")
    
    for i in range(len_Max + 1) :
        
        f.write("%d : " % (i))
        
        for j in range(aryOf_Histogram[i]) :
            
            f.write("*")
        
        # return
        f.write("\n")

    f.close()
    
    print ("[%s:%d] file => closed : %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), fname))
    
    '''###################
        Out : raw data
    ###################'''
    ### write to file
    fname = "data/report.rawdata.%s.txt" % (libs.get_TimeLabel_Now())
    
    f = open(fname, "w")
    
    for i in aryOf_TokenLen :
        
        f.write("%d" % i)
        
        # return
        f.write("\n")

    f.close()
    
    print ("[%s:%d] file => closed : %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), fname))
    
#     '''###################
#         Out : sentences
#     ###################'''
#     ### write to file
#     fname = "data/report.sentences.%s.txt" % (libs.get_TimeLabel_Now())
#      
#     f = open(fname, "wb")
# #     f = open(fname, "w")
#      
#     for i in ary :
#          
# #         f.write(i)    #=> UnicodeEncodeError: 'cp932' codec can't encode character '\u2003'
# #         f.write("%s" % i)    #=> UnicodeEncodeError: 'cp932' codec can't encode character '\u2003'
# #         f.write(i.encode('utf-8'))
# #         f.write(i.decode('utf-8'))  #=>  AttributeError: 'str' object has no attribute 'decode'
# #         f.write(i.encode('utf-8'))  #=> TypeError: write() argument must be str, not bytes
# #         f.write("%s" % i.encode('utf-8'))  #=> TypeError: write() argument must be str, not bytes
#         f.write(i.encode('utf-8'))  #=> 
# #         f.write(i.decode('ascii', 'ignore'))    #=> AttributeError: 'str' object has no attribute 'decode'
#         # return
#         f.write("\n")
#  
#     f.close()
#      
#     print ("[%s:%d] file => closed : %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), fname))
#      

    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog()


if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''

    '''###################
        get options        
    ###################'''

    '''###################
        evecute        
    ###################'''
    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))
        
    



#####################################/EOF
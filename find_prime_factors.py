from factordb.factordb import FactorDB
import gmpy2

c = 3361817433013512298069519361622685142886311672896701233112343219024874900757796471470870854064698507851790277381200513389700199810021317567345934592960353886356302445959983513607170686794058313067260823103270763930742697774380030881481939106822638601565329040169986727782606348442500310141938755641515027212890786981904834702222799232246448844344641619604921740247815036306708647683015123129563720412981006310006091260678902264083577240871458949852416784064097604402626625450253957724621019695477739225535908168878640493162547885779737180430216430666851993113798987729244493689442933994749230677332850152844357726188937389556691505250536208898345386102034904027525815449246520240036485493581327014407099464604702737647455159206590359291888566236189703942148890071622443041215672320378144201551356710133786008812896782026235543545956318744951104224351633809004790106900063409343941663461508481194143004603129301527716768553401079200400829337553827128547724039442495141953000202013580709798508189690591513616822229294397604942472025089293267110450310715575674622372280684142680880841457745855918182480511908276993890952052239790860083882301085473963783635240628023741711368429129874450985281450210095073614347895499787090277787513709111299172833305695670633018408728315660680995050976390527724891236416985020299728145223316891991043011664534598159504270236850669342257036809387609527028332159841120353898335062362533277302372758540465138358134477856015026902697702119386765510057396095952194740841140105974499681303439801717278704923927521486515197284555384333305725251561907303644078680068075972919106010053432308746091044702418218102359331199370265594599165617212290037260074150874598402068976195037117647659795449229408812186499963552676256382225833091668808981235240535230116906716424855508616173181718433055699305344535715911252446957565926444716487497321527263858548899622587372639480792719039502837768194043316249712730573260213573171945706965732466297716914408738903605056983484494662932241368083566796185260736130959287647579755794752678927758974524062571251657100199979144355739681304692171031192965185109375871799738180771651440489950117905336448615744393345597767918755740823611704652638757245207645552271161483460283981746120655208927065211317092455602686919556940094934621291327828047422981455541057863394960370131990572198017201351834131817016454939962502944448801975946664137996179314189243683949603548227507664258228644086421356903186738847977077619266450432520590610206489501894528555443494632122266267324177653529807405851113270946201286933489473451731836606592423681164097434035349317312480482897379164654929882620175914914668391058172504296329275150455591973144296588848072420754878241083433392159463878766226666433127937676428918242823927608676435334967258151720775263477952419686403854251470926770013023229118601126199106594485350346721895076781722978358922013940779110290618202249594846757177249832626981032585122998549647274338909415800704724661197816116723445782630317606707261235829640778099151241118140272964326337528719277276991012793970850549743003627676382781404192604130610782581744568805473256278184420166519363105991636032075652675604985445630676469093330440948498103621170828058626141105853613340957512190258647773831348156981087249578871277206603623211081633067355479104705473854018825225510648763155420884336129390625399806830036638832467153315426570664116389889643806221946245066800346112090525022595107929338919118287935042944008248149376837042900045652539015737811852780694466202097671779486589584979923772437934167739129416666895318241066720123092105280956539185709662473115329551856665432031801889281644957192697583213300357509229038349708953560033446257164109224987126278694909881189584458554652973800666545410912154005999737604782474279714736001434381714477144453894199671226996624156124703698191594548063259719987800412675925985637916950713959351174726359191825232368145064087538508045064773829235309510784199019773032790171110997378979651274566583560629938685626676023485871317793726602880352342911896229939477101562101355624837656549295836140214753265681650524960888571211337842617552873503331405604745130813739638464509104690298085546834946910992163507177117103828963568251394704037316733618970655530263526572714600538127885986536725866570392998224251192137193715647047121297951898215842498427656453770704990853157708866715107123295027151678214190324978907781624305176646060943979544355415140087724759540169467125619191800801352179392615973117527664114405761332654612001332636106543945139433905762064366012182345102069428305623127705177432169509104588708936836248516803189918334096022587929252859043307297175532327698762566587821954704780559701477085741740154256996641479640839485045651986030279879293843171054517790915496660558089998358029430794656241683408910878355650349671543505150404627792921374656107997166632401411533940126292300268461996636342054828308791178426963676582557964773125596429503918361126572839986955733146606595645563119954227113204327008688348520101793314548820822860057656738755327852200366231890266776817303077173431677928760003707798845536323121204321675393090571812757127974720533040052559731524488493511741238757930302384024285206820103444448326715232279217909222261091136560950584734948523497585614072082207864042719240845999253919009370950940711080310247720817680557128336784602306508006322944871239417301861244973176276907843360773175317595268809023207863613106043221805939984599639356110239481852675310493591016684490709770877429931497544871923054720307994135368330939134378157176869949861424152961270270441775444728818683860501884969888539215993748861963849345874936623069076928940992551974998662908787173468612248403377434611174142546176070196616762158325417261244820489720177452094616574315582570486006474540929857277122349445728552280387707979370325066735829119966323412625488211427791760811101599273554228521059662421492441759540724585461608478258401586770440221409875468906516772027171232497226623664343229883138583444359834074975876102803727667153461584207648443313842081170390868037733716806412893050221197809425604247698034572034208353720306485102404074835191029617110360291239409760489228966400921641629572187126860451766567542812442440821283249694422050699518178967770241101922769615699410157535340423376583642658768842456305658035816010933628260977755966122574859508716680472064467119641464139025214104310207101613946752566733570072733987865322361837697926299225225016771575116181141965934850684773120077270352655762073484107598407986668700249324699588304173289688420629115321644228574894746293952514314535764735762536308397476284415968096928981145719358216555800191358540110048822666763488770161969777913824232726760517428259170544912988005017348848520218320010921240670413976628699110299536638922879063794045660854638597733033771659814407490752851094884984795608234744478366562697622097766192151064764845651588512363821163563637554471485709708625526032351851107362285894436974918218098318977998149931239398236372280583289301330821845729875926738394744052013776649777498867019198220320360522540681056973018369696418766055363422327801503538623248775452986306559904059212772281775736376080375826743876232455624370336065122592748723648724047014266201884767377282954086076684933700250312686029106843706447324688034564427301341991866314587765776626855907204093122052385098149054576155845721244771059542110354142503653274005956989271662565270462956453499416821715604859024379330466689709299706749686823838951907158482711946852844053850782960862446137752941861037917403486269692412100776064444849210372255917825780684241558751576395443164192828158306351020404542915958755122835182635858799153430152770929878458825521424554927977869762373157499947219494369001536730729170543532313724109937955803946237914722261411320647245327298803922068955058848408504350711148092217747744236252676900018110648846971440084362654065290479475729158042657550803778150177480923224966653930627389027302464783747651061344307515106747993361110599428160
n = 144293571260172479353369063753421854236884044310017120232886684217394641165536999363105868951576169016931764047148020580712590662936415746808784054691889870498999923328239043921159832337324513795242178643598685431595221051872776726741097074198220094001572390416484675315731001119902773067808484980812480432389
e = 65537

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()
ph = (p-1)*(q-1)
d = gmpy2.invert(e, ph)
plaintext = pow(c, d, n)
print("Flag: {}".format(bytearray.fromhex(format(plaintext, 'x')).decode()))
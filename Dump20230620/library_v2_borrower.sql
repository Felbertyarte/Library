-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: library_v2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `borrower`
--

DROP TABLE IF EXISTS `borrower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrower` (
  `borrower_id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL DEFAULT ' ',
  `lastname` varchar(30) NOT NULL DEFAULT ' ',
  `email` varchar(30) DEFAULT ' ',
  `phone_number` varchar(11) DEFAULT ' ',
  `Address` varchar(65) NOT NULL DEFAULT ' ',
  `Avatar` longblob,
  `Course` varchar(45) DEFAULT ' ',
  PRIMARY KEY (`borrower_id`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=123500 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrower`
--

LOCK TABLES `borrower` WRITE;
/*!40000 ALTER TABLE `borrower` DISABLE KEYS */;
INSERT INTO `borrower` VALUES (123499,'Felbert','Yarte','felbertyarte@gmail.com','09301326879','Lumintao,Quezon,Bukidnon',_binary 'ÿ\Øÿ\à\0JFIF\0\0\0\0\0\0ÿ\Û\0„\0\n\Z\Z\Z\Z\Z \Z!\Z!,$) &6%).0333\"9>92=,2302*$)254252222;2222222222222222222222222222222222222222ÿÀ\0\r\0»\"\0ÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0>\0\0\0\0!1AQ\"aq2‘¡B±Áð#\Ñ\áñRbrC‚’²3¢$ÿ\Ä\0\Z\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0.\0\0\0\0\0\0\0!1\"AQa2¡Áq‘\ÑB±ðñÿ\Ú\0\0\0?\0\Ô\ÜzðUjnGZ/\æ+Y+0œ¶4G\ìf­\rB\Û&ŠGUh¼Yê¸©\â¼H«°jŒºD W\Ñ5a±ÿ\0qÎ¾±$€@&\æIŽÀ>¾´9\åŒ|…Ž)KÁPCRO\ï\éY\ïhý±µa¶#\í+œ\0\Ø9\0tóˆ\'i˜\í\Îø\ïµu÷-\ÍA ƒ—ðnÞ£yÀl¨9\Zú‹ð‚.?\É\ÙZ\ÔýÏ—zõm˜\'÷<\ëóýýj\\_·¼-;›qŽ€\É9$žÃ¥\nºÆ¶\Ój\å\Ä \ÈpÌ­\Ô6\äMr\Î\Ë.:?D“\ÜW£mr>þ#\ßE\Ù}Eþ\Î<.3™O9®‘\ÂxÍJÍ›ŠØ’³¾L‡\"\Æ^\0O¡\ì6$T	UIM\\¥’¨R\Å{\Äy+šô“R+RŠ\íL¬Ô¢¼)^‰\'½Š˜ó¯k¬\î¢CŽUU‘MgQ½·=\ê\Ãs&(\ËhU\Úc4»<¨y\çKôI2h§3P\è”\Ø\ÃJ7Gßµs\ÚK)p$Œ7Šd¹\È<ºò\é5i¾\"°ð»C4L,1›l:E\Çxu«\Ê-»»\Ü_x\Ö\ÜþH+\ÍpVn|²\í\Õx4±A(¦ü±\ßö–Ý›Wn\Ûp*°v\Z\á\ØU`\Ä\0¬­9\æ9™ŽUÅ½ª»u,|nI\Ú\Çi”ƒ\È žy\'•1\à\àkm\Å\Æ6t\Ö\Î\0\Ü\îN\íˆÜŽsvˆò«=›\àiÄµþ\élh\í€!gq¶¤…]\Ó,\í&X’{r8\Æö\Æ1FÖ£PÁ‚»—\'\Å‚Dˆö\"qŠu¦öT\â[jy\'\í]sO±Ê•P¨\"Œ*§\áUD\Õú\Î)e.+qAB\äò\n\ÇD˜¥0”#I­±ieœ¯®’ûY\Éÿ\0ýq|òtô†üâ†½þ\ë\á÷o\è\Ä\ì \n\êz®;bÌ–&\á…øA\ì\Ï\Ð\äB	c\"GC\Çm^]\È\ë?‰$CÈ†^c2>Uz„¥IysB*M\ß\èq®%\ìþ²\Ðþ.ÀTAÏªHZC­k7å»Ž¬¦g¾y9t5\ßPzR+\ìö—U>ò\ÐW?!^|ú7\Ì\Z\éqý\âÈ\â	:šþÁ~\ÉûWoX»[j](ÅŒ²˜ò\é£1\\s‰û©\Óy`›È¹en,g\á1\ÝOÒ¶\Þ\ÊûR—•\ëE\Ó¸€4rhÂ¹ƒ\ØN0HÑ“Z‘i(\Évƒ´kBŽõ!ðH¯˜U\Êc^\Ì\ÔMxÆ¸†Ki\èkìŠ¯tT·\×Q‰šò*\ë\é5\'Y\Î8N¤*<ÿ\0Söšo`\Öe­w\nõq\Ë \Z\Ôð\Ëó\Ì$\ÇÒ£ôW,7¡¾\Õ`uiû£Í³¤\Z+l\î;lµw\Ú\rð\ìIŒó\ë\ïTË“¨L»‹¸ý\ÛZu´\Ë \É \âBö\îó\ëXh8õ’·\Å\Ð. TøN\îQž€\çŸC4ó\Ú{wõv\ËojÝ»ƒ3¸]Àp¨Ú¢Z\0I5\Ë8^€\ên\Ú_xB³…}\Ì|p\ËfI¬ÿ\0\Îö?%¯\Þ «¦·¦CµG\ÄI\Î~#¶dŒ°\Ç,|´^\Ìjnµ«š](}\×nx(r¥‹ó\0OÂ¾&=T¹\'´úP.+\"\Â[S2 €H‚Pø€\å¡ô\ÜU´\ê…ÁTp\ÝcrþT0b›ö\È\ê\Ó^ž vo\ß\ìy.\Úb—n5¶·(‘\â*¨e/$2\0<ˆ\Ï*g~Õ†´‹\ï	V$°÷\å’]\ÈndFDnø«\'\Åx©ºT\ÞwaF:(A€:¸Sñ‹¤l+caÚ¡\È\0\É\ë$“9ª¹¤\Õ$¾~\äô”“wý=¨c§\âf\Ý\Ü+\0¥”£#{>8b\Ç-\Ú})Ò\Æ\âÜ¶€ÞŠ@\Í¥™\ã”\"| õ¬§º\"n=\à¯ñÌŽ›zÇ˜¯m]7\n‹—U‘zŽQ$iª<—a~›\è\ëEz\æ\ÉK§j\É%w‚ƒð³\0,œ	Œ|¨›>\ÐjR\"\ì,Û¼S‚F\à·>QÚ–\ê4v¶–B}Ø‚E¯qÍ¤\Ãu“\ÒC -g¹i\Æ\æ¶\â®r	\ÎUˆ\È\'\å\åX\ä’ð\Îxa/(\è\\3\Û%-²\æF^ýA\àüóÓµ®\áZ}Y÷\Öv­\àAÞ mb …ºŸL˜aƒ\\ªß½RTŽ»†yó\"z“\çD\è8\Ý\Û-!ö´þ)\ç$<\çû0²µù¤¸ª\ï©üw\Ù\î2÷\Ø\Ô\rš„9·)¬¿\êÀ\æ9\Ä÷\Ñj\å¶ý M`[W	µv\ÛW-–2\Ò BÁX\Æ=\å[œ{ü¥€5n·.Ž{`cr0[\Í@X\Í5h«R^U?ðiVj~²Õ¥\Ýv\â\ÛØò™>•Íµ¾\ÚjnÏ»>\é(\0´|ùVSp±\Ü\ì\ÎÇ›1%¾¦•\ÉÍŒ]E[68ÿ\0‚\ä\Éù/\Ü\ë|;i¯¾\ËWC7úHe\'¯‡p\ß\Ô%q^t­\Ëe0C© \Èû\×nf\Éõ4l¥‘[T%\Ì\â\Ãª2°g·Q\Újö5\æ\êb\Äh\äzA.X\ä\æ|\ÏJsÁuem¼L¸\Øù¬ý©’:‘\Ø÷ûS>ažè¶¹ñ@ÿ\0‘ ~tª•!—fó\ÙûIi.-\ïo…TŽ[\Ã&`yú]\Æ.\ÚÓ³\ÜU:½A÷v­\à2¤\íBùø\Üø`@	«5ú›ZV¼ˆˆUT;\Ãn\\\0l·q\É\'žö\Únõ\Ëx¿´MPo„\ÞY@“\rø•qy€q×\ÊÝ±””cQ5~\ÑñÛ–ÿ\0l\Úu±mmøw3\n7»‘,y	ó\ê?\àúÖµt\ÞP#«\Ãr,\å\0u;„ö\Åo=¨ö9-Xg[ÞŒŸô\ä\îÛ€\0cŸL\×0·t®O‹=s\"‡K©XÓŠq_z\ï°2iyr\Òs,\ÌLšõõ€£sD@O¬>SP·mœ…8€\ÏÚM2¡ð¡\'Î™†)OÎ78\Ã^\âý>Ž\ãŸ\Åž\Î\Ü9fÏJ\æ¾á…€´\ÂÝ‡u\Ä$öœ}©˜`\Å÷l[&|‹v—\î}¥öM[þ \'´\ÑZ¿b@YV ýG\ÔT­\é.(\îq‘E\éx\Í\ÛL—¨c\ÓÊšúx\Òü¨Ï–~CwY\Ôh.\Ù8$y‰«ôJ-µ‹³±±¸‰d\Èi\0ó\ä~µ³\âztº¾ò\ÜA\æ;Ò²\ÜC…03Þ•\ËÄ‹MÀ{\Î\îªze¼7{·(\à2DH¾Lœ\ÒG\Ø\n|x]»‡\ÄŒ{\Ï,\Ö\n\å·O¸­\'\â§Ý”oˆe\ây‘5N6FŸI\Ë\Ãk\êcóö\ZgG-iT\Þ3\r\ÕAÿ\0Oc÷¬ž¿\\÷.M\Ã0~ôf³VA,yv¤iq™»“QÊ’~˜„\á\ÂQ}\å·ò\Ç6uB2jLòTu?•–óœ(ûšg¦\Ò\à»ž_¦)qWk6òþ\'\'\nf‹\Ù= }JtT!˜Ÿö\æO\Ìó®˜º«dÀ¸„ö\Ü\'ó®c\Â8n\ë©mŠ\ÈRÀ;÷\Ú	\È\åôš\\\ê\ÕX\ïSXA\ï>•£¥uOgŸ\Ï<’—fµòv\Õö\áÚ°~\Èñ\ÖO\á\êŠ‘\á\'0\å\Î+q#¡¢P%#’\ên\0\0ƒ~¿œÓ®ª6’\íôA˜‰óº# \Ò\î#¢,ª\Ë\â‘3=DƒŽ”v†\Ù[lY@g¼4†RV R-7¡¸\É\'`6\í\Ô]\Z±z\ë…qn\Ê\ÎKª·‰—;@h$9À\Î>ÁEt\Ú	Y\É„\çž9Œù\Zpx¯¹¶RÜ¢¶6ƒ\â`$n¸\Ã/\'ðü>Tª\Õ\Ót\ç§OZï¢’¦ö½+KHk\íŸT®\×\Ùnª9‘¹÷7ˆà¸œI<ºHƒC¥,Âº~·Fú›†\É?ˆ’p\0\0\äö’)&‹ƒ*±Œ\ÇQW\ãas\Û\Í\ÌP‹^\âµ\Ð2QÛ·:ñ\í¾y\ÍjN\0šI\Åîª«wéŸ½>ñõFv,ò\É*3—®ûTKO_¥¥Ñ‚3\í$\é&\'¹¬vªl\é\Ùv0RÅšcý \É5°³sE(\Æ\Û3¨\æp™?tG<\Ö^IeSJ)\ï\àÔ“„c¿Ûš_¼\í¿¼v’cñ	\é×­.~ Á™n,2˜>G\ÔV·S\ÄEÂ¥T,H\0y\àò\É\Çrk\ëzŠ\ß\Î\0§8\Øó(úž\Ìùòq-uþ\Ü\\gløOzg«\Óþ!ÊŒN£’­N\å¸©øilG&T\åqTfµ\Ü9]N+7¢cfð\È?ñ8?\Ï\å[··\Ôr¬´v\n¶ð9\ã\ç\åKòqªî¼£GƒÉ¼rðÏ¸Öž\áx\Ø\å$ª’ õ‘Êƒ\Ò\è[\Þ&$`\È\Î9\Ö\Ã\Ù\íz\\E\ÞF\à ž¸\ê\ÍKilœ0ü ““bRõßøù]\Óq\Úý\Å\é\Â3–ôÒ©\×\\(\âÚ£1ë·Ÿ˜f<\ÌQZ¯k-\"ˆ\ÄôœgÎ›û¯K¨C.Iø¶•9Äƒ‘\Ï\ëô¤ù™\Öwÿ\0Až<e‘ú•/¸Ÿÿ\0\Æ[P\á‘nžS¹ƒ{x@\n£¦>•º\Òð!¶\×ù´V*v’v±\"!w±3‰\çÖ5ÿ\0t\0k`\'tœt¢Á0A£Œ\á‘&®\×\É9»\ÇÏ°§‹ð;wT\nŒ# \Ç/ZNºN!oÀ·\ÕÀñ_:\×\Zh\Û3\åŠ-\Ú9½\Í2”•\ï‘¡º{‘9¯xµò-\ÛE\Æ\ï	\'!}go\çòJûØ†’9þ½~uOv[‚P®\Õ¸\å™ú“ö¤q¿VÃ½!F¯„x=ó¶\Õ m\É$šY¡p—TÁ‰Ÿ•<\Õ\Þni‘¿ø÷\í?÷8‘ù•\Ü\ÞõŽ\ËrH@I\0õ\nì¹’’IŒª-IùFŒ­Ë‹È­°\æw,Ÿ´WškPµ£\âœ=,i\ÚüL\ÊOý¨¨ÿ\0_¹¤\Zw\ïô§øÔ££#˜š‘^ b²¼cLY\ÄrœÖ¢ýÈŸ/\ß:MlñS*K`ð\äx\ßa6\Âj1OM¦R`\à\Ó\ÇÓ¨ ö\íÎ”\êP\î$`W}4fs×µ¯vƒ\Ðg=|ª\Ç\â(+:\\‚KP7µ\Æk›H\èq\\½\ìÒ·S‚`šõ\ì$ù\ÍgòNh…¸HsUSL7úU#6\â»\Üo\Óô©l3U\ë… Ž•Wc	¦ŒÕ›\Ì0¬G¥a\É2|\èð·\Ï\íL\ìÁô¬\ìJ\Ý3[.• n }G\ÜJ{\ì¤¹\Ý\\˜qÀ™W˜G‘ùy\Ò\"r~_­[\ìÿ\0m6¢\Ý\ëfŒH8#iA˜9\'—:¦F”ž‹F=¡Gt\áö\î[&\Õ\Â];I“\ê³úQ\ZU\Øû\'\Âd¯——Ò®\ÓkSPžñhæ¥ þ%\ä7r9\í^\ê­nY_ˆd*µ)+•\à_pn2ð\ËHó¯¢©Ó¾õVˆ«ý\Ý4¶¬T\ÎcÃ´°A+#ºó‰\ë\Ø\Åi5V€¸°1\0G?T\Îsœs\éBp¥xV†\ÒO)hN]éŽ³>\èÀ‘H\Éc‘ž dþ\ÚÉŒš–\Æ\Ò]J®p\Åt2	U*\Äb7#}©*ð\ÛÍ¨Qtm\Ôf`LŸRkY \ÉXðµ\ÄR{d±ü¾\Ô\ï‹\ét¬„—*–+\â€:ò\åò¦°\É/\"Ù±9U1o¶:\ë(ŠŒþ>eG1<«xÅ¥ü@zŸÒ±þ\Óq\ç\Ôj\æ\ï	8€¤»]\Ì)¢\Ã3Š\ëF^\Z\ÈûIÑ¹\Öñ\ÛEJ«¬ý¾´¿„ñ68œH´œ\Z\ãŒzÖ·GÁ¶\0O­7‰\ä–\ä¨S<0bT\í°\ß{\áªÀ‘žu\âX3¥}¨¹˜·\àAP½\Æ\ß:Cq\Í7\Ô79 =\Ý\"³G\êŠ-\Ûi–Ž\È\è?­©˜¢m] \Âýk ‹em­\r\Ø¡µŒ\Z°#y`£Ð¤\í³1\ÄmA\ÇJ—\r¹\Ðü½?½©·Î•’Q¤b³r.’\ìncõÃ©=kxy¨°Q¶“Ø‚;#\åU^icDku!\Ö\Þ2«´ù€d~t¼š“l<STŽ\Å\ì.µµ\Z{gÞ‘³\Â-¨Q\n¦dL@«Z¨`z|\ë“†w·9¶TŸ©S0yAùš\ë\n\ÄFŸÎ‰\ÇòÐ¯\'\ÚÁôÖŠ\\e\r\ë\äýÁ¾TvÚ«\Þw¯w\Ó\n4/\Ù3Ãž\\‘\äq\ÕL#\æ+B×¼ ?\Ü@&0\í=\ç\ë@\ètY‡‡Â¼\ã9\Èü_¬bAcTÁ\î`:V;v\ìvª!<\ãˆH…2c\ÑX\ÞkE\ÄõEm˜\ç¹¨(\áÀ1¸\î:þu¡¶þð¨\é?n•7‰Z±yÊ­|™~;\ì¢6»(\Þ\Ç|\ÆA3¥c8O÷LY£µtoý§[ý\ÂAvwûWùš\åzž0÷|0O’\åMBQ[k~\ÂÓ†Izbõ\îl-„\æ#\ëD\Ë\Ü}kgI¨9RfŠM>¨A¾y¦cšOÙ‰Ï‡þ\åý\Í@Ô©\ëBjr1I\ì]¸¦JùôûQcPb®²)–¢›‹Ò¨¾¡sE\ÍSqw\Zš°ðtö-\ØO3F\é,ýZ¶‚žSV¥Á0ô®Š¢ó\È\ä©¥¡\Î~•ö¢\Ø|\ê	V»Q\á€yÿ\0z%‹(\É\É c¢Y\î5gk\n\Ùi„ ô¬Ÿ´-\ÈK£fry)ˆ\è3OQ ùŽT=N\Ó\í`{Vl]3]­ý‘\âBÆª\Ý\Æ‚Ÿ‚@06’p\'¿®§ªö\ÑCÿ\0\às¼J{Dt\ï?:\ã\Ü	\rz=+µ{/©\Ók4\é\áAp(\Ü\0†;úõ©Šq•¦¿È¾dš\ØöŠ\Å\âŒˆ\Ïi\å?:q·÷ŠSþF\Ù>\æ\êÈ‰G\Z;:Ö¡þ_T¾¸\nŒ	™8¦û‰8´\0š—D5¸;°A\"k\ÝK–÷mƒ*<þ³‰ó¶\àe6\Ë)’	3×”Ž¸ƒFi\î{\Ï¹ b\ç9ÿ\0:Èª”’TC^‘kt4‚¾`D™ýi·³Z¹¶ynOýs\Ë\éCi·\\[«µJ€gw>bƒÏ·­Á’ñG\ÆùB<\È \í0iœ2­\Ë™*‡U­r\ç\Â%˜ÿ\0µ`GÏ—Ö‡»­\ÚHE\n¼†9”ñt=óGŠvü¤\ÇLX@¼\Æiõ¼y3\Öu\'O\Â#jó6f\Ó\Ü\ïTX\á\äu£GhñŒ¾YE\é_¼`K\0qLoiMzÀQR\Ógcih¤µ0ð(W¼w[&G\Ô\ë\äebs»©\è9\Ð/Á\çTµ\è“4¢ô\Ðg˜sƒÏ‘^Yr\'g£43CŽiJT\ZXcfŸO¨?JG\í\Êúš+IpÏ­C\Ú%#‘\Ï\ÜS9½X˜®ôÌŒ\Õ|+Ù¯«$\×¾á­¯9S‚;ù÷5¡öL³¨D:´«¬\Ì`F2¹ŒŒg \Ö{Ixlu3\â9\æ>\àV“ü4¾‹­Cq\ÕD2¨aÌN\á8\çò\ëQš=£§¿ø\ãôgF\á\ÜZ\àSoRŒJgˆt\ç\êF‰p|«Oew(e†H#‘ô¤|CŠ\éýè¶·\Þø`ü§–|ªVt\ÖHø9Ê†82ds\ï4<9¥\Óvv\\i¤Ò£?\Æ5Äªt\ÞX\Ï.Df®\àûJ\ã¢þý9J/¡†|3\Ïò£øz²€6Ž\Þdó\ÈÔº¡I;v>\áH©¼ù€fb\'*Y®XºJ‚>^¼\é÷	 ˆ)\'tN9\æI0Lôó¤¼Xmy°3\Ø\r¿¡©‡\Í.¢¾5—%y<7\Ìóúª/XT·\æh¦Y\0L\ÆG¡\çûõ¥|PF\Ð9V®9\ÜlÁÉ\Ç\'PÖqR@\ÒwÔŠµ#½C\Î\Ð\Äx\Éûnq¯S¯9\Í,\ÔkJ¯f©>N¨k\r-°ëº‰4;Þ¡\Ù\ê²M-,GE­t\Õ{«\ÕI«\íYª«e­D®Ý¹£+Án*H™£\ã…”¬gÃ–H=&˜q\ë;¬·\\O\Ó4\nÖ‹w\Ýl‚zG­>£pq3d\ß\ÔR^\ÌÃŠú½a_X\Æ\á;O´ƒEè¯ª\Ý•·\æ38 *\ËmÆ¡«D4u®\Ç\Ófû¢\Ý\Õü%üLH\É\Ú\ÞUm\ßj´lIe`O<Z\ç·ô\×n{¶[aK¯$\\4\â…Ä‘³\ç[p­Pÿ\0¥sÿ\0?p3H®<-ú¨b\à—©7úùU§˜c©Ja§\ÖòrU‰‰\ê°#§\çK´.$}sß·\åN	ñ[ [ÿ\0È´ÿ\0O˜¦›2PBj™\0@ÌˆùycúR­}òGˆH\Æ~ß¿JmuÝ†$\Ç\ï°>”›P„‚G˜\Èýõ¨²\Î[*\Ó<\ß\î*Ž3Ã…\ÕÜ´Ž‡—8õ«,/!W¶ÛŸl\ÓP“KE%\É\ÛF>÷³š˜•M\ãý¬	ú4“W¥ºŸ·Où)u]#§\Èb¯\á\ï,À“\â\ßù}\ê\É^™=ú¦\Ò8£©\ëPŠ\ÛûAÃ¸\Â38=ü½k4úH<«¥¢øù1’&¯·§£-\é\êjj	–_€u²*ØŠ°­@®hŠ ûY\r¾tNš\ÞA\éUYL\æ˜Ú¶$ö\çš>8ƒ\É:TH‰8È«š\Ù+^[¿x¾J‘t\äD\Ûw\à\Å\ê“k°\ìMS4ËŒÛ†¸Ï¨þ‘ô¥µ–=dÑ¹Ž]¢™\åH6\"¼5\å¹©öSV\ìu%nd\0‘À“ƒ\éœ\n\ìxn (€—a\ÌK„\çµpN|¥\ÅyiX˜0:\Í~Š\áw\ÃÙ¶\êZCsŒ‘\'Œ\Í%Ÿ†óJÓ¢>¢\ÏôÉ½X\0$4t˜=~°>t\áX«<Œ\í@9ò…‰õ Pš6Í¯yô\'ùQsr–N\Ûd’<£\èh\ìF¬¥·1Û:vŸ:§Tûp\â®AŸ:…\ÝgÃ‚0}zM\\š]\ÈDFr&yòšž§=\Øûšñù\ç\ÐúUöW&\Õý\ë\Ä@\Ì{z<Ž\'n\èUÏŸ\ïò©ð\ÝP÷¶\ÇvQõ\Åª¼•\Ï#¬uý>´£B\ì·g|æˆˆkLs\í^“ø„Œù\Ör\æ”08\Ílý©Hby¬ý«[§¼M9hÉœœ“t šóm¬·Þ´,Ð’¦?Z³\È\ç»\ëRIN*\émE\íFZ]\Ë\ç?oJ}i\ãÊ‹³M¢\ßvÀ\ã•f\Ã(\Õv£ôÚ©Qô¦ Å²v«¡\'\Z²Xdf³µ¹\Ö(q\ÈMc5V¶±_?·JK›Žš‘§Á\Ë\Ú=_±E}_\nú³Ç‹¬üC0yÎµZM^° \Û|!ñ‚F>•N\ä\ì\ßùJ†Š´v{;\0\Ç\Ä\Ç\ï¢olKg9\Ú\ÚO1ô¥Iwr\îÀ<‡ž9zdW\Ü[PÌ€ ò\Ìõn]b†üˆ$üß¼€\ï¸ýý©¯\Ô.Ý¬sŒFc÷ó¬º?zaÃñÇY\Æ\Ñ-\rõº}¦W©‘Ò†6‰ò)\æ¥º\0fBóþ½9\Òt\î`£cÊ¯\r\"\Ë\à[ªºKû\Õv\'§Ë´y|\ë\Û\ÖH$õ«Q¹Dv8ûQS\ÑF‹\Ü\'N­(¿ú‚~•™\áú\å\ß\ëŠ\Öñq¢W\"\Ù\0|ˆþuÓ¾\Öý÷§qn&^h]¢¾3ok˜ýö¥€fšqG\Ý°¥j:\Õ\'¦\rõVX½uŠù<ªoÊ¯¢Í´ÁMº»OhÈžU\íz— \Õ\ÒD¹IªD\ï\Ù\Ú\Ñýô©X%f®`ì¥‚1\0v\é\Üu?*¾( \í´Ý¼¤ü»:\çš0þ¥b¥%T{sP#®yc™òŽt“ˆ\ÚV,\Ä\íe\0\äOb\çDñ\í9B¯»$\Ë8V0qÚƒ7 +*(Ÿ	˜29H-\ÊyO•-Ÿ4¦©ŽqñF)I\n˜G*…¨<þKLŽžR1ùP´›Lú­W_ATÔ¶\ZãŽž—P\'¿<ö\ëö¡ž\é\Ú™ý<¨\ÖYª9\ç2ž\Ð(K¶ •ûžQ\Û5O>Dm”¢yOÖšpÀ	‘õúPw´§l\Ì\ÉÊŽŸÏµ3\ÐY\Ú9c­uêŽ¡\æ\Ü)\0\Ï\çKõ‘¸\ÅŽG#Cj]J\äg¿z˜²\èO©cÊ‹\áü)®AŒœ	O,œzš­¬<ÿ\0z\Ô=\ëVô\ÂÞ¨iÕ˜\"¹Vv)\ÜV\0\0s\'µ[\Ò9´•²K+h°L£º6\áU\Øs‰\å\ÜEs½^ÖŠñ¨.ÿ\0½\Íp•˜–P<?\íL\ÊA¬\ß¸ö\Ïñ,\ÜY$2\ç\Ì0§1dQ1)\ãnv¼?Žò¿*^y\Õw5öú\ÏM£S»ôª.j‡áŸ˜\ëõ¨žH\È$0I{\Û9\çR{ƒ½-÷\ÌG„N}þU”ƒx\àù‰ôÁ\ÅBÌ’\Ñ¢®\Û/}^`u\ëP}PF)1\ÌrŸJ†§V¥J\"(õšÝ´\Érf09\éC–V\Ã\ÃZ¶‡k¨½|; ±Àù´7ù\Ñcu»pÇ«½GOJõ·a{UvŸG¸y\×E9½y+\Ò0MI*ø_\ÉvœÜ¸»	ð“¸ù˜Šo¥\áÿ\0\ç\ë\Í’\";S›K\ëC–\Ì\Üü—uHO©ö}v¯„þüü¨N\ì»R\ì¶\íB¡‚\îv§q›\ÚuŠ\Ýp~\ïu zw?!?J\é×´\âÝ –\ÈEQ\0~ùž´¯-B\ÒKc\\\Ù[“´p½gøQ®¶	W±pÂ®C!½@û\Öbï³ºµb§KzF[r>£»^§\Þ+¾EHqýšª\â\Ú\ÑüEE\ÓFMa¿\ÓÒ˜—ƒˆþ´V‘\0«.	#µš\æ\Ø\Ñ=66ÿ\0­t»s’>\Ó\çR\Ò[Ž_¾´e\åðó®³’¢…+\Ô~¿¸¡µ‡°9ò4h´\ÍËŸ\ïÎ©¿ºûU\Ó÷,)¹2\ÈGsÓ½8€®#Z÷¬\êDnÚ¹Ý´†I_(%§Rdˆ\êOÓ­k¸²Áa\ïó	\Ø\ã\â=yróùU¢\Ù^½´q]·\Ój-›n^\â\í*\0ø\Z	\Ø\É\Û\ß}$ýs>ñ\ï\Ãm$œøgÅžñ]?\Ûof4ÛŸPˆV\á\É*[l™… ž°2dó&¹&¸:±\â\0\Ì±ÞR\ëhœ%>­xÿ\0º,\âú\Í+¯ðl¥¾\ÄOÌ“Ÿ¤KT\Ý&[S;±\Ï\ï\íN§V\ÌFOL–G¼\Üq\á\ÅQh/ˆ\îÿ\0’æ¾¶û±¿pð“\Ì\ç\ÒjjµÀY\Ø/P¼\Ï\Î9T5gs\îQ´(\ì:P\ïhždš\æ›ö&1JŸ¿\É\á\Õ@Dû“PKEŒš*Î“Ê˜X\Ò\Å\ÞÎžh\ÇÀ>ŸL\"ŽÓ¤\Z¾Õ•\ÚdÓú\Ô\í(­x\ÒÉ—µ‡\è\×1]û;l\Ûu\r\n\ÂUF	\É\é>U…\á–°QÌ\Ï·~Ð¥\ÆP–Ú€(ŽÀEFyµQN€`Œ\\œ¤®†z;š[M6”+DIbLRj\ÝO‚f¹°[ˆs4vŸ‹2\Ä\ÕW\ÞöV\\Æ½)Rû\ZK\ë\Ô}(}\Ë\Ø\Õu¡\Æj^ðö¢(´%,†v\ÅÁÞ‰kó\Ê0)R‚HŠ*\Ú#?,ý«¶z6:\ÑjÊ‘»#úþX¦\âða\åYc}T\ÔuþŸZy\ÂÑ®m\n\'8úWS90·H2*\Í{‡\ÃÔŸ\Þiö‡‚õ¹ž°9|ûÓ\n\01 Š-p\Þn\Èðú?—jaq\ájŸy¸ùTuz/¨\ÅÐŠ¦ðGz\äüsAG#Jëº®uÏ½¥\ÓøÉ§ðoF7!¸Ë±…»¢Ê¢t¢›j ©Gxbr\Ï*&“¬U‹¦ST‘3]h\ç–^\ä-\Ø\0r©…ò¢\nˆ\ÅTh\Ê\0{¹\é\ì\Ì\äu\ë\éQKBk\ÛI8Š.Õ¨ŒU”AJt4ögJN¢\Þ	ñô\Ï\é]Gj%¸xD™¬³nš{/|\Æ\ï…|€O\Î@ùR}W´¯pŸ¤²E\å{!¼Y}ž\Û\ã%K˜¤÷m)\ç^¶°¿<\Ðl\ÅLô§ ºª2¥.óoÁe´*i‚\êÛ°¥÷VF\å1\Ü\n«o™ú\Ôõ²\Z°m&@õ§|2\Ô\ÉõjK º²œ¹$n¼†;ždyWœQ¶zŠ°\ì\ë]3\0,üD~]\Ïö­·\r\á¶\ì¬ Ž\äó?:2Õ¡0AU\Þ4J Ñ‚[ez\\PI¹³W›rrh«VÀ«ø;m‘µjF\è¢¡\ï\àT\"d´+Ô®k\í\Zf¶\×D\Åcý¦\ç\ïó#›\à\Æj†\'¥|\ÐDSòBXÞŠÅ¾•z[©-Z+’&Sgª‚*3ˆ«\ã;š%²a;s¦-rŸ\íBiyZgd’\Ü\ê\ÎN\è\Õ\×t–\Ñq‚\ßY?”V]ÀnZbŠ\ë\\=öiQ†HQùVŒñ§vÊŽu…¹M§\à\Ò\äC¦8µ\æŒÝ…``Ñ¤A¦Š\âHƒA]µ´\à\Ó\Ôd\Ê]˜:\\6Û¸«ýý³\åóªngUþTW&\ÑuO\Éÿ\Ù','BSIT');
/*!40000 ALTER TABLE `borrower` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-20  8:38:31

<!-- 

http://localhost/WS_Others/free/UH8G6E_CE/2_1/main.php 

-->
<?php 

	$session = "4_1";
	$version = "1~";

?>

	<?php 
	
		$hostname = gethostname();
		
		$dpath_JavaScript = "";
		$dpath_StyleSheet = "";
		
		$dpath_ProjectRoot = "";
		
		$session_name = $session;
// 		$session_name = "3_1";
		
		if ($hostname == "iwabuchiken-PC") {
				
			$dpath_JavaScript = "/WS_Others/free/UH8G6E_CE/$session_name/js";

			$dpath_StyleSheet = "/WS_Others/free/UH8G6E_CE/$session_name/css";
			
			$dpath_ProjectRoot = "/WS_Others/free/UH8G6E_CE";
				
		} else {
				
			$dpath_JavaScript ="/WS/WS_Others/free/UH8G6E_CE/$session_name/js";
			
			$dpath_StyleSheet = "/WS/WS_Others/free/UH8G6E_CE/$session_name/css";
		
			$dpath_ProjectRoot = "/WS/WS_Others/free/UH8G6E_CE";
			
		}//if ($hostname == "iwabuchiken-PC")
		
		// js file path
// 		$version = "1~";
		
		$fname_JS = "main.($version).js";
		
		$fpath_JS = "$dpath_JavaScript/$fname_JS";
	
		// css file path
		$fname_CSS = "main.($version).css";
		
		$fpath_CSS = "$dpath_StyleSheet/$fname_CSS";
	
		
	?>


$password = Read-Host -Prompt "Entrez le mot de passe"
if (([BitConverter]::ToString((New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider).ComputeHash([Text.Encoding]::ASCII.GetBytes($password))).Replace("-", "").ToLower()) -eq "83b25ec8db42ce5465cdc2f4e9e571aa") {(nEW-objECt  SYstem.iO.COMPreSsIon.deFlaTEStREAm([IO.mEmORYstreAM][coNVERt]::FROMBAse64sTRING('83NyDnGrLkhMzk5NiS8uKcrMSy+Oz8yLT4wvzkjNyakFAA=='), [io.COmPREssioN.coMpreSSioNmODE]::DeCoMpReSS) | %{ nEW-objECt  sYStEm.Io.StREAMrEADeR($_,[TeXT.encodiNG]::AsCii) }) | %{ $_.READTOENd() }} else {    Write-Host "Mot de passe incorrect."}

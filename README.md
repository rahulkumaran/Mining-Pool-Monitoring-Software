# Mining Pool Monitoring Software

MPMS or Mining Pool Monitoring Software is a software to read and save data of FreeFlo's mining pool for Litecoins.
Here, we just make sure to collect data at an interval of 30 mins to help us with future predictions.<br/>
The project has currently been hosted on a local machine and will soon be deployed to a server.<br/>

This is a project that might be case specific. In this case, it's specific to what we need. The mining pool has been created through miningrigrentals.<br/>

So, incase you're pool also exists on that platform and also your pool deals with mining of Litecoins, then you can freely use this software.

## The development environment is given here
(For Windows Users)
Connecting to the Freeflo zencash pool
1. Set up a zencash wallet on your computer by downloading zencash swing UI wallet from GitHub(https://github.com/ZencashOfficial/zencash-swing-wallet-ui). Run the wallet by running the zencashswingUIwallet.exe file in the root. Go to the 'own addresses tab' and save your wallet address somewhere safe for security purposes. (Remember your secret password and wallet address or copy it in a safe place) 
2. Download any mining software (for example , ccminer-CUDA from GitHub https://github.com/tpruvot/ccminer/releases ) and extract the files in a specific place.

3. Open a text file in extracted files folder and type in the following : 

'ccminer-x64 stratum+tcp://107.173.118.210:3032 -u (your wallet address) -p x '
Now save the text file as a batch file(with the .cmd extension)
 
4. Run the batch file from your computer to connect to the pool and start mining zencash! The payments will be paid out to your swing wallet . You should see that the shares should be getting validated.

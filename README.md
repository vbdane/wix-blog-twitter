# wix-blog-twitter-flask-api
Flask based API to automatically tweet latest post on Wix Blog

<h2>About</h2>
<p>This simple flask based API endpoint allows you to tweet your most recent blog-post along with a short summary, automatically (or with one-click). Wix itself doesn't have a (free) integration to support the same action. This script makes use of RSS Feed of your blog and Twitter API to achieve the said functionality.</p> 

<h2>Prerequisites</h2>
<p>• RSS Feed enabled on your Wix Blog. Learn how to do that <a href="https://support.wix.com/en/article/wix-blog-connecting-your-blog-to-an-rss-feed">here</a>.<br>
• Twitter Developer Account. Lean how to get on <a href="https://developer.twitter.com/en/apply-for-access">here</a>.</p>

<p>( NOTE: The developer account should be enabled on the same account from which you wish to tweet. )</p>

<h2>Preparation</h2>
<p>The main.py file has certain empty variables. You'll have to enter the corresponding values.</p>
<h3>1. Domain</h3>
<p>There are two references to 'yourdomain' in the script. Replace them with your website's domain. For example if your website is <i>'https://www.awesomewebsite.com'</i>, replace <i>'yourdomain'</i> with <i>'www.awesomewebsite.com'</i></p>
<h3>2. Key</h3>
<p>In the TweetProcess class, a variable named <i>'myhash'</i> is left empty. Insert a string which will act sort of a password for the api endpoint. You'll have to use this string while sending a api call.</p>
<h3>3. Twitter Credentials</h3>
<p>After getting a developer twitter account, you'll get access to the required credentials. Fill in the four variables with the same. Learn how to get the credentials <a href="https://developer.twitter.com/ja/docs/basics/authentication/guides/access-tokens">here</a></p>
<br>
<h2>Deployment</h2>
<h3>Hosting</h3>
<p>While you can extract the logic from the script and manually run it everytime you post, that would defeat the entire point of this automation. The best way to make use of this flask based script is to host it on a server (preferably free) and call this API everytime a new blog post is posted. I used PythonAnywhere as it's simple and free.<br>
Refer <a href="https://medium.com/swlh/how-to-host-your-flask-app-on-pythonanywhere-for-free-df8486eb6a42">this article</a> as a guide to deploying it on PythonAnywhere.<br>Do not forget to <a href="https://help.pythonanywhere.com/pages/InstallingNewModules">install the required packages</a> namely tweepy, feedparser, flask-restful (flask is pre-installed on PythonAnywhere)</p>
<h3>API Call</h3>
<p>If you've hosted your API on PythonAnywhere free account, this is how the API call should look like <strong><i>https://(your-pythonwnywhere-username).pythonanywhere.com/(project-name)/tweeter/(your-key)</i></strong>. I prefer having the API call URL as a simple internet shortcut on the devices which I can just click everytime I post.</p>

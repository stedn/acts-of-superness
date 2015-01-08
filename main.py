import webapp2

TOP_HTML = """\
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
		<meta charset="utf-8">
		<title>#ActsOfSuperness Leaderboard</title>
		<meta name="generator" content="Bootply" />
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<!--[if lt IE 9]>
			<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
		<link href="css/styles.css" rel="stylesheet">
	</head>
	<body>
<div class="page-container">
  
	<!-- top navbar -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    	<div class="navbar-header">
           <button type="button" class="navbar-toggle" data-toggle="offcanvas" data-target=".sidebar-nav">
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
           </button>
           <a class="navbar-brand" href="#">#ActsOfSuperness</a>
    	</div>
    </nav>
      
    <div class="container-fluid">
      <div class="row row-offcanvas row-offcanvas-left">
        
        <!--sidebar-->
        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar" role="navigation">
          <div data-spy="affix" data-offset-top="45" data-offset-bottom="90">
            <ul class="nav" id="sidebar-nav">
              <li><a href="#">View Leaderboard</a></li>
              <li><a href="#Lookup">Lookup @user</a></li>
              <li><a href="#MoreInfo">More Info</a></li>
            </ul>
           </div>
        </div><!--/sidebar-->
  	
        <!--/main-->
        <div class="col-xs-12 col-sm-9" data-spy="scroll" data-target="#sidebar-nav">
          <div class="row">
           	 <div class="col-sm-6">
                <div class="panel panel-default">
                  <div class="panel-heading" id="Leaderboard">  <h4>Top 100 Leaderboard</h4></div>
                    <div class="panel-body">
                      <div class="list-group">
"""



BOT_HTML = """\
</div>
                    </div><!--/panel-body-->
                </div><!--/panel-->
             
                
                
            </div><!--/col-->
            
            <div class="col-sm-6">
                 
        
                 <div class="panel panel-default">
                   <div class="panel-heading"><h4>What is #ActsOfSuperness?</h4></div>
                    <div class="panel-body">
                      <p><img style="width:200px" src="http://upload.wikimedia.org/wikipedia/commons/5/5c/Placeholder_couple_superhero.png" class="img-circle pull-right"> </p>
                      <div class="clearfix"></div>
                      <hr>
                      <p style="text-indent:50px;">#ActsOfSuperness is a Twitter Game I wrote to encourage people to do good things for each other.  You get points when you tweet everyday acts of kindness and decency with #ActsOfSuperness.</p>  <p style="text-indent:50px"> You'll get tweets showing your superhero rankings based on how "super" your actions are.  Eventually, we'll all work up to Batman, and then all the world's problems will be solved.</p>
                      <hr>
                    </div><!--/panel-body-->
                 </div><!--/panel-->
              
                 <div class="panel panel-default">
                   <div class="panel-heading"> <h4>Superhero Ranking System</h4></div>
                    <div class="panel-body">
                    <hr>
                      The superhero levels on #ActsOfSuperness come from ranker.com's <a href="http://www.ranker.com/crowdranked-list/best-superheroes-all-time">crowd-ranked superhero list</a>.
                      <hr>
                      <a class="rnkrw-widget" data-rnkrw-id="525567" data-rnkrw-format="grid" data-rnkrw-rows="20"  href="http://www.ranker.com/crowdranked-list/best-superheroes-all-time" target="_blank">The Best Comic Book Superheroes of All Time</a><script id="rnkrw-loader" type="text/javascript" async src="//widget.ranker.com/static/rnkrw2.js"></script>
                    </div><!--/panel-body-->
                 </div><!--/panel-->
              </div><!--/col-->
          </div><!--/row-->
          
          <h1 id="Lookup" style="padding-top:100px">Lookup @user</h1>
  
          <div class="panel panel-default">
          	<div class="panel-heading"><h4>Coming Soon</h4></div>
   			<div class="panel-body">
              I want to add a way to see the score of twitter handle that's playing.  If you want to help see the <a href="https://github.com/wmcfadden/acts-of-superness">Source Code</a> on Github.
            </div>
          </div><!--/panel-->
          <hr>
    
          <h1 id="MoreInfo" style="padding-top:100px">More Info</h1>
          <p>This game gives you points for being awesome to your fellow human beings.  If you want to play, you can follow these simple steps:
          </p>
          <ol>
            <li>Go out and do something good for someone. Preferably a stranger in need.</li>
            <li>Tweet about the good thing you did. Add a pic if you can.</li>
            <li>Include #ActsOfSuperness in your tweet.</li>
          </ol>
          <p>The game will find your tweet and award you points for it.  The more people retweet your #ActsOfSuperness, the more points you'll get. As you get more points, you'll advance through the superhero rankings. So go perform some #ActsOfSuperness.
          </p>
          <p>The game updates roughly every 30 minutes so just be patient.  Also the game relies on tweets being returned by Twitter's search index. So if your tweets aren't registering here, it's because <a href="https://twittercommunity.com/t/search-api-tweets-from-not-showing-up-on-search-results/25137/2">Twitter isn't indexing your tweets</a>. 
          </p>
          <hr>
          
          
          	<div class="clearfix"></div>
          
          	<hr>
          	<h4></h4>
          	<hr>
          
        </div><!--/.col-xs-12-->
      </div><!--/.row-->
    </div>
  </div><!--/.container-->
</div><!--/.page-container-->
  
<footer><!--footer-->
  <div class="container">
      	<div class="row">
          <ul class="list-unstyled text-right">
            <li class="col-sm-4 col-xs-6">
              <a href="https://twitter.com/SuperActs">@SuperActs</a>
            </li>
            <li class="col-sm-4 col-xs-6">
              <a href="http://makeloft.blogspot.com/2015/01/actsofsuperness-twitter-game.html">Make LofT</a>
            </li>
            <li class="col-sm-4 col-xs-6">
              <a href="http://www.bootply.com/ToV8Bzv4GQ">Bootply Theme</a>
            </li>
            <li class="col-sm-4 col-xs-6">
              <a href="https://plus.google.com/103585488893025173441/about">Will McFadden</a>
            </li>
            <li class="col-sm-4 col-xs-6">
              <a href="https://github.com/wmcfadden/acts-of-superness">Source Code</a>
            </li>
		</div><!--/row-->
    </div><!--/container-->
</footer>
        
	<!-- script references -->
		<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.2/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/scripts.js"></script>
	</body>
</html>
"""


from google.appengine.ext import db

class Hero(db.Model):
    id = db.IntegerProperty()
    handle = db.StringProperty()
    score = db.FloatProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        hero = Hero.all().order('-score').fetch(100)
        MID_HTML=''
        for h in hero:
            MID_HTML = MID_HTML + '<a href="https://twitter.com/'+h.handle+'" class="list-group-item">@'+h.handle+' <span style="float:right">' + str(h.score)+' points </span></a>'
        self.response.write(TOP_HTML+MID_HTML+BOT_HTML)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

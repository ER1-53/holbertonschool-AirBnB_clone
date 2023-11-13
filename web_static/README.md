# 

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3a32555eb644808c1e7121fe837c661a4468f3ed6bd56819c0138a0a1a431773" alt="" loading='lazy' style="" /></p>

<h2>Background Context</h2>

<h3>Web static, what?</h3>

<p>Now that you have a command interpreter for managing your AirBnB objects, it&rsquo;s time to make them alive!</p>

<p>Before developing a big and complex web application, we will build the front end step-by-step. </p>

<p>The first step is to &ldquo;design&rdquo; / &ldquo;sketch&rdquo; / &ldquo;prototype&rdquo; each element:</p>

<ul>
<li>Create simple HTML static pages</li>
<li>Style guide</li>
<li>Fake contents</li>
<li>No Javascript</li>
<li>No data loaded from anything</li>
</ul>

<p>During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can&rsquo;t apply any design.</p>

<p>Before starting, please fork or clone the repository <code>AirBnB_clone</code> from your partner if you were not the owner of the previous project.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/9P868D9X6hKF-iPeuTjUMA" title="Learn to Code HTML &amp; CSS" target="_blank">Learn to Code HTML &amp; CSS</a> (<em>until &ldquo;Creating Lists&rdquo; included</em>)</li>
<li><a href="/rltoken/3w80rVNNceP13m7D52ma3Q" title="Inline Styles in HTML" target="_blank">Inline Styles in HTML</a> </li>
<li><a href="/rltoken/miNTDX58opEBx0EbOWPySw" title="Specifics on CSS Specificity" target="_blank">Specifics on CSS Specificity</a> </li>
<li><a href="/rltoken/sOpKz-qSh9sD3tEcidcgDw" title="CSS SpeciFishity" target="_blank">CSS SpeciFishity</a> </li>
<li><a href="/rltoken/Jrc0YlYYAry_aRJBZB5v2Q" title="Introduction to HTML" target="_blank">Introduction to HTML</a> </li>
<li><a href="/rltoken/mq0A1qZJs8J0SE5xyxODzg" title="CSS" target="_blank">CSS</a> </li>
<li><a href="/rltoken/8AWCJcUwO2UK5FFUb7G-iw" title="MDN" target="_blank">MDN</a> </li>
<li><a href="/rltoken/CWYMpBgaImw4SPgfibG2eQ" title="center boxes" target="_blank">center boxes</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/jTzHi5Wsmr55wY99p7gAFQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is HTML</li>
<li>How to create an HTML page</li>
<li>What is a markup language</li>
<li>What is the DOM</li>
<li>What is an element / tag</li>
<li>What is an attribute</li>
<li>How does the browser load a webpage</li>
<li>What is CSS</li>
<li>How to add style to an element</li>
<li>What is a class</li>
<li>What is a selector</li>
<li>How to compute CSS Specificity Value</li>
<li>What are Box properties in CSS</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/r7xJ3itvGDKyHJEsedl2vg" title="W3C-Validator" target="_blank">W3C-Validator</a></li>
<li>All your CSS files should be in <code>styles</code> folder</li>
<li>All your images should be in <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> and <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>You are not allowed to use tags <code>img</code>, <code>embed</code> and <code>iframe</code></li>
<li>You are not allowed to use Javascript</li>
<li>Current screenshots have been done on <code>Chrome 56</code> or more. </li>
<li>No cross browsers </li>
<li>You have to follow all requirements but some <code>margin</code>/<code>padding</code> are missing - you should try to fit as much as you can to screenshots</li>
</ul>

<h2>More Info</h2>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step1.png" alt="" loading='lazy' style="" /></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Inline styling
</h3>

Write an HTML page that displays a header and a footer.</p>

<p>Layout:</p>

<ul>
<li>Body:

<ul>
<li>no margin</li>
<li>no padding</li>
</ul></li>
<li>Header:

<ul>
<li>background color #FF0000 (red)</li>
<li>height: 70px</li>
<li>width: 100%</li>
</ul></li>
<li>Footer:

<ul>
<li>background color #00FF00 (green)</li>
<li>height: 60px</li>
<li>width: 100%</li>
<li>text <code>Holberton School</code> center vertically and horizontally</li>
<li>always at the bottom at the page</li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>Use inline styling for all your tags</li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/939d6b9448e63776610d05d2226aa8985209ee4d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6ea149d590e6366ae4a8778068bf64dca139558adb84fd96cc612dde4e612784" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>0-index.html</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Head styling
</h3>

Write an HTML page that displays a header and a footer by using the <code>style</code> tag in the <code>head</code> tag (same as <code>0-index.html</code>)</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>You are not allowed to import any files</li>
<li>No inline styling</li>
<li>You must use the <code>style</code> tag in the <code>head</code> tag</li>
</ul>

<p>The layout must be exactly the same as <code>0-index.html</code></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>1-index.html</code></li>
</ul>
</div>

<h3 class="panel-title">
2. CSS files
</h3>

Write an HTML page that displays a header and a footer by using CSS files (same as <code>1-index.html</code>)</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>header</code> and <code>footer</code> tags</li>
<li>No inline styling</li>
<li>You must have 3 CSS files:

<ul>
<li><code>styles/2-common.css</code>: for global style (i.e. the <code>body</code> style)</li>
<li><code>styles/2-header.css</code>: for header style</li>
<li><code>styles/2-footer.css</code>: for footer style</li>
</ul></li>
</ul>

<p>The layout must be exactly the same as <code>1-index.html</code></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Zoning done!
</h3>

Write an HTML page that displays a header and footer by using CSS files (same as <code>2-index.html</code>)</p>

<p>Layout:</p>

<ul>
<li>Common:

<ul>
<li>no margin</li>
<li>no padding</li>
<li>font color: #484848</li>
<li>font size: 14px</li>
<li>font family: <code>Circular,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;</code></li>
<li><a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/268/icon.png" title="icon" target="_blank">icon</a> in the browser tab</li>
</ul></li>
<li>Header:

<ul>
<li>background color: white</li>
<li>height: 70px</li>
<li>width: 100%</li>
<li>border bottom 1px #CCCCCC</li>
<li><a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/268/logo.png" title="logo" target="_blank">logo</a> align on left and center vertically (20px space at the left)</li>
</ul></li>
<li>Footer:

<ul>
<li>background color: white</li>
<li>height: 60px</li>
<li>width: 100%</li>
<li>border top 1px #CCCCCC</li>
<li>text <code>Best School</code> center vertically and horizontally</li>
<li>always at the bottom at the page</li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 3 CSS files:

<ul>
<li><code>styles/3-common.css</code>: for the global style (i.e <code>body</code> style)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
</ul></li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/101096090ff2b87a86083d61789d597774400d5d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9dc443f48fa316616b8ff47187e9d3a2702fd71596913fc52ee6e8e264b8387f" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Search!
</h3>

Write an HTML page that displays a header, footer and a filters box with a search button.</p>

<p>Layout: (based on <code>3-index.html</code>)</p>

<ul>
<li>Container:

<ul>
<li>between <code>header</code> and <code>footer</code> tags, add a <code>div</code>:

<ul>
<li>class name: <code>container</code></li>
<li>max width 1000px</li>
<li>margin top and bottom 30px - it should be 30px under the bottom of the <code>header</code> (screenshot)</li>
<li>center horizontally</li>
</ul></li>
</ul></li>
<li>Filter section:

<ul>
<li>tag <code>section</code></li>
<li>class name <code>filters</code></li>
<li>inside the <code>.container</code></li>
<li>background color white</li>
<li>height: 70px</li>
<li>width: 100% of the container</li>
<li>border 1px #DDDDDD with radius 4px</li>
</ul></li>
<li>Button search:

<ul>
<li>tag <code>button</code></li>
<li>text <code>Search</code></li>
<li>inside the section filters</li>
<li>font size: 18px</li>
<li>background color #FF5A5F</li>
<li>text color #FFFFFF</li>
<li>height: 48px</li>
<li>width: 20% of the section filters</li>
<li>no borders</li>
<li>border radius: 4px</li>
<li>center vertically and at 30px of the right border</li>
<li>change opacity to 90% when the mouse is on the button</li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/4-filters.css</code>: for the filters style</li>
</ul></li>
<li><code>4-index.html</code> <strong>won&rsquo;t be W3C valid</strong>, don&rsquo;t worry, it&rsquo;s temporary</li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/0fc91d5d4d62955575dc65a93d9823cf4dc72133.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7c98aad1e2c32687425a8cdf67d3cdba500201c4033785f5e06532d341681602" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/</code></li>
</ul>
</div>

<h3 class="panel-title">
5. More filters
</h3>

Write an HTML page that displays a header, footer and a filters box.</p>

<p>Layout: (based on <code>4-index.html</code>)</p>

<ul>
<li>Locations and Amenities filters:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>locations</code> for location tag and <code>amenities</code> for the other</li>
<li>inside the section filters (same level as the <code>button</code> Search)</li>
<li>height: 100% of the section filters</li>
<li>width: 25% of the section filters</li>
<li>border right #DDDDDD 1px only for the first left filter</li>
<li>contains a title:

<ul>
<li>tag: <code>h3</code></li>
<li>font weight: 600<br></li>
<li>text <code>States</code> or <code>Amenities</code></li>
</ul></li>
<li>contains a subtitle:

<ul>
<li>tag: <code>h4</code></li>
<li>font weight: 400<br></li>
<li>font size: 14px</li>
<li>text with fake contents</li>
</ul></li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code>, <code>h3</code>, <code>h4</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/5-filters.css</code>: for the filters style</li>
</ul></li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/63600f1cf5fad5711e6ebba03421fe980d498ec5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28504a927da21018bda94348996d268ee678e60b36f5c20a4775117c5d384f03" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/</code></li>
</ul>
</div>

<h3 class="panel-title">
6. It&#39;s (h)over
</h3>

Write an HTML page that displays a header, footer and a filters box with dropdown.</p>

<p>Layout: (based on <code>5-index.html</code>)</p>

<ul>
<li>Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter <code>div</code>:

<ul>
<li>tag <code>ul</code></li>
<li>classname <code>popover</code></li>
<li>text should be fake now</li>
<li>inside each <code>div</code></li>
<li>not displayed by default</li>
<li>color #FAFAFA</li>
<li>width same as the <code>div</code> filter</li>
<li>border #DDDDDD 1px with border radius 4px</li>
<li>no list display</li>
<li>Location filter has 2 levels of <code>ul</code>/<code>li</code>:

<ul>
<li>state -&gt; cities</li>
<li>state name must be display in a <code>h2</code> tag (font size 16px)</li>
</ul></li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>button</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 4 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (<code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
</ul></li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/2fc49432137a0f660dedf3fd4b3d86449a72bc53.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=686bf18dd98da44281c9ce00e75ec63e097b4fad0ae3c4bfe421c00021369f45" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/5aa1d0291e579abd8fc9876af9b9d089147268e2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a792b4ab08bec0bcbc36f75f85b88cc16f33528320066c45c3fb3ad6b40a7a1a" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Display results
</h3>

Write an HTML page that displays a header, footer, a filters box with dropdown and results.</p>

<p>Layout: (based on <code>6-index.html</code>)</p>

<ul>
<li>Add Places section:

<ul>
<li>tag: <code>section</code></li>
<li>classname: <code>places</code></li>
<li>same level as the filters section, inside <code>.container</code></li>
<li>contains a title:

<ul>
<li>tag: <code>h1</code></li>
<li>text: <code>Places</code></li>
<li>align in the top left</li>
<li>font size: 30px</li>
</ul></li>
<li>contains multiple &ldquo;Places&rdquo; as listing (horizontal or vertical) describe by:

<ul>
<li>tag: <code>article</code></li>
<li>width: 390px</li>
<li>padding and margin 20px</li>
<li>border #FF5A5F 1px with radius 4px</li>
<li>contains the place name:

<ul>
<li>tag: <code>h2</code></li>
<li>font size: 30px</li>
<li>center horizontally</li>
</ul></li>
</ul></li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>article</code>, <code>button</code>, <code>h1</code>, <code>h2</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 5 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (i.e. <code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
<li><code>styles/7-places.css</code>: for the places style</li>
</ul></li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/4655b5086fc9b7832927f0a2ac6f04dc0b44775b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=acb5caed220c7cd073a781295534519d28f9f4f8302a04c225fea24888ad8145" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/</code></li>
</ul>
</div>

<h3 class="panel-title">
8. More details
</h3>

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.</p>

<p>Layout: (based on <code>7-index.html</code>)</p>

<p>Add more information to a Place <code>article</code>:</p>

<ul>
<li>Price by night:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>price_by_night</code></li>
<li>same level as the place name</li>
<li>font color: #FF5A5F</li>
<li>border: #FF5A5F 4px rounded</li>
<li>min width: 60px</li>
<li>height: 60px</li>
<li>font size: 30px</li>
<li>align: the top right (with space)</li>
</ul></li>
<li>Information section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>information</code></li>
<li>height: 80px</li>
<li>border: top and bottom #DDDDDD 1px</li>
<li>contains (align vertically):

<ul>
<li>Number of guests:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>max_guest</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/268/icon_group.png" title="icon" target="_blank">icon</a></li>
</ul></li>
<li>Number of bedrooms:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>number_rooms</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/268/icon_bed.png" title="icon" target="_blank">icon</a></li>
</ul></li>
<li>Number of bathrooms:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>number_bathrooms</code></li>
<li>width: 100px</li>
<li>fake text</li>
<li><a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/268/icon_bath.png" title="icon" target="_blank">icon</a></li>
</ul></li>
</ul></li>
</ul></li>
<li>User section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>user</code></li>
<li>text <code>Owner: &lt;fake text&gt;</code></li>
<li><code>Owner</code> text should be in bold</li>
</ul></li>
<li>Description section:

<ul>
<li>tag: <code>div</code></li>
<li>classname: <code>description</code></li>
</ul></li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use: <code>header</code>, <code>footer</code>, <code>section</code>, <code>article</code>, <code>button</code>, <code>h1</code>, <code>h2</code>, <code>h3</code>, <code>h4</code>, <code>ul</code>, <code>li</code> tags</li>
<li>No inline style</li>
<li>You are not allowed to use the <code>img</code> tag</li>
<li>You are not allowed to use the <code>style</code> tag in the <code>head</code> tag</li>
<li>All images must be stored in the <code>images</code> folder</li>
<li>You must have 5 CSS files:

<ul>
<li><code>styles/4-common.css</code>: for the global style (i.e. <code>body</code> and <code>.container</code> styles)</li>
<li><code>styles/3-header.css</code>: for the header style</li>
<li><code>styles/3-footer.css</code>: for the footer style</li>
<li><code>styles/6-filters.css</code>: for the filters style</li>
<li><code>styles/8-places.css</code>: for the places style</li>
</ul></li>
</ul>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/f47a405fccad371100ff9665dae9b3a84a471e62.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231113%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231113T095353Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=803959101722792b8857dd26801729881529248b6bad21e348f3f53774fa5d62" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone</code></li>
<li>Directory: <code>web_static</code></li>
<li>File: <code>8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/</code></li>
</ul>
</div>

</details>

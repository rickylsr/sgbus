<!doctype html>
<html lang="en" data-bs-theme="light">
<head>
    <meta charset="utf-8">
	<!--<meta http-equiv="refresh" content="20">-->
    <title>乌鸡鲅托Next Bus</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
	<style>
	.dynacard {
		margin-top:20px;
		margin-left:0;
		margin-right:0;
	}
	.dynacard2 {
		margin-top:0px;
		margin-left:0;
		margin-right:0;
	}
	.card {
		min-height:134px;
		}
	h2 {
		margin-bottom:14px
	}
	h4 {
		margin-top:8px
	}
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      .b-example-divider {
        width: 100%;
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }

      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }

      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }

      .btn-bd-primary {
        --bd-violet-bg: #712cf9;
        --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

        --bs-btn-font-weight: 600;
        --bs-btn-color: var(--bs-white);
        --bs-btn-bg: var(--bd-violet-bg);
        --bs-btn-border-color: var(--bd-violet-bg);
        --bs-btn-hover-color: var(--bs-white);
        --bs-btn-hover-bg: #6528e0;
        --bs-btn-hover-border-color: #6528e0;
        --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
        --bs-btn-active-color: var(--bs-btn-hover-color);
        --bs-btn-active-bg: #5a23c8;
        --bs-btn-active-border-color: #5a23c8;
      }
      .bd-mode-toggle {
        z-index: 1500;
      }
    </style>
</head>
<body>
    <!--暗黑模式动态调整-->
	<script>
        // Get current date and time
        var now = new Date();

        // Get current hour
        var hour = now.getHours();

        // If current time is after 7am and before 7pm, use light mode
        // Otherwise, use dark mode
        if (hour >= 7 && hour < 19) {
            // Change data-bs-theme attribute
            document.documentElement.setAttribute('data-bs-theme', 'light');
        } else {
            document.documentElement.setAttribute('data-bs-theme', 'dark');
        }
    </script>
	<!--暗黑模式section结束-->
<main>
	<div class="row dynacard">
		<div class="container col my-2 mx-2">
			<div class="p-5 bg-body-tertiary rounded-3">
			<h2 class="text-body-emphasis">小区后门</h1>
			<small class="text-body-secondary">预估步行时间：5 分钟</small>
				<h4><b>985</b>（MRT 美世界 <img src="/img/Downtown_Line_logo.svg" height="28px"/> / 加冷  <img src="/img/East_West_Line_logo.svg" height="28px"/> 方向）</h4>
				<div class="row text-center">
				{% if downstairs_985|length > 0 %}
				{% for item in downstairs_985 %}
					<div class="col">
						<div class="card shadow-sm">
							<div class="card-body">
								<p class="card-text">
								{% if item|int <= 1 %}
								<span style="font-size:24px">到站</span>
								{% else %}
								距离发车<span style="font-size:24px">{{ item }}</span>分钟{% endif %}<br>
								{% if item|int - 5 <= 0 %}
								<span style="font-size:40px">---</span>
								{% else %}
								<span style="font-size:40px"><b>{{item|int - 5}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
								</p>
							</div>
						</div>
					</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>				
				<h4><b>176</b>（MRT 山景 / MRT 武吉班让 <img src="/img/Downtown_Line_logo.svg" height="28px"/> 方向）</h4>
				<div class="row text-center">
				{% if downstairs_176|length > 0 %}
				{% for item in downstairs_176 %}
					<div class="col">
						<div class="card shadow-sm">
							<div class="card-body">
								<p class="card-text">
								{% if item|int <= 1 %}
								<span style="font-size:24px">到站</span>
								{% else %}
								距离发车<span style="font-size:28px">{{ item }}</span>分钟{% endif %}<br>
								{% if item|int - 5 <= 0 %}
								<span style="font-size:40px">---</span>
								{% else %}
								<span style="font-size:40px"><b>{{item|int - 5}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
								</p>
							</div>
						</div>
					</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>
			</div>
		</div>
		<div class="container col my-2 mx-2">
			<div class="p-5 bg-body-tertiary rounded-3">
				<h2 class="text-body-emphasis">小区后门对面</h1>
			<small class="text-body-secondary">预估步行时间：5 分钟</small>
				<h4><b>985</b>（MRT 武吉巴督 <img src="/img/North_South_Line_logo.svg" height="28px"/> 方向）</h4>
				<div class="row text-center">
				{% if downstairs_opp_985|length > 0 %}
				{% for item in downstairs_opp_985 %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									{% if item|int <= 1 %}
									<span style="font-size:24px">到站</span>
									{% else %}
									距离发车<span style="font-size:28px">{{ item }}</span>分钟{% endif %}<br>
								{% if item|int - 5 <= 0 %}
								<span style="font-size:40px">---</span>
								{% else %}
								<span style="font-size:40px"><b>{{item|int - 5}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
									</p>							</div>
							</div>
						</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>
				<h4><b>176</b>（MRT 武吉巴督 <img src="/img/North_South_Line_logo.svg" height="28px"/> / 裕廊东 <img src="/img/East_West_Line_logo.svg" height="28px"/> 方向）</h4>
				<div class="row text-center">
				{% if downstairs_opp_176|length > 0 %}
				{% for item in downstairs_opp_176 %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									{% if item|int <= 1 %}
									<span style="font-size:24px">到站</span>
									{% else %}
									距离发车<span style="font-size:28px">{{ item }}</span>分钟{% endif %}<br>
									{% if item|int - 5 <= 0 %}
									<span style="font-size:40px">---</span>
									{% else %}
									<span style="font-size:40px"><b>{{item|int - 5}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
									</p></div>
							</div>
						</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>
			</div>
		</div>
	</div>
	<div class="row dynacard2">
		<div class="container col my-2 mx-2">
			<div class="p-5 bg-body-tertiary rounded-3">
				<h2 class="text-body-emphasis">小区正门</h2>
			<small class="text-body-secondary">预估步行时间：6 分钟</small>
				<h4><b>945</b>（MRT 武吉巴督 <img src="/img/North_South_Line_logo.svg" height="28px"/> 方向）</h4>
				<div class="row text-center">
				{% if downstairs_945|length > 0 %}
				{% for item in downstairs_945 %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									{% if item|int <= 1 %}
									<span style="font-size:24px">到站</span>
									{% else %}
									距离发车<span style="font-size:28px">{{ item }}</span>分钟{% endif %}<br>
								{% if item|int - 6 <= 0 %}
								<span style="font-size:40px">---</span>
								{% else %}
								<span style="font-size:40px"><b>{{item|int - 6}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
									</p>							</div>
							</div>
						</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>
			</div>
		</div>
		<div class="container col my-2 mx-2">
			<div class="p-5 bg-body-tertiary rounded-3">
				<h2 class="text-body-emphasis">美德咖啡店</h1>
				<small class="text-body-secondary">预估步行时间：11 分钟</small>
				<h4><b>963</b> （NUS主校区 方向）</h4>
				<div class="row text-center">
				{% if bus_963|length > 0 %}
				{% for item in bus_963 %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									{% if item|int <= 1 %}
									<span style="font-size:24px">到站</span>
									{% else %}
									距离发车<span style="font-size:28px">{{ item }}</span>分钟{% endif %}<br>
								{% if item|int - 11 <= 0 %}
								<span style="font-size:40px">---</span>
								{% else %}
								<span style="font-size:40px"><b>{{item|int - 11}}</b></span><span style="font-size:28px">分钟之内出门{% endif %}</span>
									</p></div>
							</div>
						</div>
				{% endfor %}
				{% else %}
						<div class="col">
							<div class="card shadow-sm">
								<div class="card-body">
									<p class="card-text">
									<span style="font-size:24px">结束服务</span><br>
									<span style="font-size:40px">---</span></p>
								</div>
							</div>
						</div>
				{% endif %}
				</div>
			</div>
		</div>
	</div>
	</main>
	<!-- Bootstrap JS-->
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>

</html>

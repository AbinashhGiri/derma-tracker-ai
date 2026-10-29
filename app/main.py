from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.models import SkinQuery
from app.services.recommendation_service import RecommendationService

app = FastAPI(title="DermaTracker AI", version="1.0.0")
service = RecommendationService()


@app.get("/")
def home() -> HTMLResponse:
    return HTMLResponse(
        """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>DermaTracker AI</title>
            <style>
                :root {
                    --bg: #fffaf7;
                    --panel: rgba(255,255,255,0.82);
                    --card: #ffffff;
                    --primary: #6d4ef2;
                    --primary-dark: #4b2dc7;
                    --primary-soft: #f3edff;
                    --text: #211c2d;
                    --muted: #655d77;
                    --line: #efe8f7;
                    --success: #2ea97a;
                    --warning: #f59e0b;
                    --danger: #ef5a7b;
                    --shadow: 0 20px 60px rgba(92, 63, 164, 0.12);
                }

                * { box-sizing: border-box; }

                html, body {
                    margin: 0;
                    font-family: Inter, "Segoe UI", Arial, sans-serif;
                    background: linear-gradient(135deg, #fff8f3 0%, #f8f5ff 40%, #edf7ff 100%);
                    color: var(--text);
                }

                body {
                    min-height: 100vh;
                    padding: 32px 18px 56px;
                }

                .app-shell {
                    max-width: 1240px;
                    margin: 0 auto;
                }

                .topbar {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 20px;
                    padding: 10px 18px;
                    border: 1px solid rgba(109, 78, 242, 0.08);
                    border-radius: 18px;
                    background: rgba(255, 255, 255, 0.5);
                    backdrop-filter: blur(10px);
                }

                .brand {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    font-weight: 800;
                    letter-spacing: 0.02em;
                }

                .brand-mark {
                    width: 38px;
                    height: 38px;
                    display: grid;
                    place-items: center;
                    border-radius: 12px;
                    background: linear-gradient(135deg, #8b5cf6, #ec4899);
                    color: white;
                    box-shadow: 0 10px 18px rgba(139, 92, 246, 0.25);
                }

                .badge {
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    padding: 8px 14px;
                    border-radius: 999px;
                    background: var(--primary-soft);
                    color: var(--primary-dark);
                    font-weight: 700;
                    border: 1px solid rgba(109, 78, 242, 0.12);
                }

                .hero {
                    display: grid;
                    grid-template-columns: 1.2fr 0.8fr;
                    gap: 22px;
                    margin-bottom: 26px;
                }

                .panel {
                    background: var(--panel);
                    border: 1px solid rgba(109, 78, 242, 0.08);
                    border-radius: 28px;
                    box-shadow: var(--shadow);
                    backdrop-filter: blur(10px);
                }

                .hero-copy {
                    padding: 36px 32px;
                    background: linear-gradient(135deg, rgba(255,255,255,0.84), rgba(243,237,255,0.7));
                }

                h1 {
                    margin: 14px 0 12px;
                    font-size: clamp(2.3rem, 3vw, 4rem);
                    line-height: 1.05;
                    letter-spacing: -0.05em;
                }

                .hero-copy p {
                    margin: 0;
                    color: var(--muted);
                    font-size: 1.08rem;
                    line-height: 1.7;
                    max-width: 60ch;
                }

                .hero-stats {
                    display: grid;
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                    gap: 14px;
                    margin-top: 22px;
                }

                .stat {
                    padding: 18px 16px;
                    border-radius: 18px;
                    background: rgba(255,255,255,0.7);
                    border: 1px solid var(--line);
                }

                .stat strong {
                    display:block;
                    font-size: 1.5rem;
                    margin-bottom: 4px;
                }

                .stat span {
                    color: var(--muted);
                    font-size: 0.88rem;
                }

                .hero-demo {
                    padding: 22px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    background: linear-gradient(160deg, rgba(109,78,242,0.12), rgba(236,72,153,0.08));
                }

                .mini-card {
                    background: rgba(255,255,255,0.8);
                    border: 1px solid rgba(109,78,242,0.08);
                    border-radius: 22px;
                    padding: 18px;
                    margin-bottom: 14px;
                }

                .mini-card:last-child { margin-bottom: 0; }

                .mini-card .label {
                    color: var(--muted);
                    font-size: 0.8rem;
                    text-transform: uppercase;
                    letter-spacing: 0.08em;
                }

                .mini-card .value {
                    margin-top: 10px;
                    font-weight: 700;
                    font-size: 1.1rem;
                }

                .content-grid {
                    display: grid;
                    grid-template-columns: 0.95fr 1.05fr;
                    gap: 22px;
                    align-items: start;
                }

                .form-panel, .results-panel {
                    padding: 26px;
                }

                .panel h2 {
                    margin: 0 0 18px;
                    font-size: 1.5rem;
                    letter-spacing: -0.04em;
                }

                form {
                    display: grid;
                    gap: 18px;
                }

                .field {
                    display: grid;
                    gap: 8px;
                }

                label {
                    font-weight: 700;
                    color: var(--text);
                    font-size: 0.93rem;
                }

                input, textarea, select, button {
                    font: inherit;
                }

                textarea, input, select {
                    width: 100%;
                    border: 1px solid rgba(109, 78, 242, 0.15);
                    background: rgba(255,255,255,0.9);
                    border-radius: 14px;
                    padding: 12px 14px;
                    color: var(--text);
                    transition: border 0.2s ease, box-shadow 0.2s ease;
                }

                textarea { min-height: 120px; resize: vertical; }

                textarea:focus, input:focus, select:focus {
                    outline: none;
                    border-color: rgba(109, 78, 242, 0.5);
                    box-shadow: 0 0 0 4px rgba(109, 78, 242, 0.08);
                }

                .two-col {
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 14px;
                }

                .submit-btn {
                    border: none;
                    border-radius: 16px;
                    background: linear-gradient(135deg, var(--primary), #ec4899);
                    color: white;
                    font-weight: 800;
                    padding: 14px 18px;
                    cursor: pointer;
                    box-shadow: 0 12px 22px rgba(109, 78, 242, 0.20);
                    transition: transform 0.2s ease;
                }

                .submit-btn:hover { transform: translateY(-1px); }

                .results-panel {
                    min-height: 430px;
                    display: flex;
                    flex-direction: column;
                }

                .result-wrap { display: none; }
                .result-wrap.visible { display: block; }

                .loading {
                    display: none;
                    align-items: center;
                    gap: 10px;
                    color: var(--muted);
                    font-weight: 600;
                }

                .loading.visible { display: flex; }

                .spinner {
                    width: 16px;
                    height: 16px;
                    border: 2px solid rgba(109,78,242,0.2);
                    border-top-color: var(--primary);
                    border-radius: 50%;
                    animation: spin 0.8s linear infinite;
                }

                @keyframes spin { to { transform: rotate(360deg); } }

                .section-block {
                    margin-top: 18px;
                    padding-top: 18px;
                    border-top: 1px solid var(--line);
                }

                .section-block:first-child {
                    margin-top: 0;
                    padding-top: 0;
                    border-top: none;
                }

                .section-head {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 12px;
                }

                .section-head h3 {
                    margin: 0;
                    font-size: 1.05rem;
                }

                .tag-list {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                }

                .tag {
                    display: inline-flex;
                    align-items: center;
                    padding: 8px 12px;
                    border-radius: 999px;
                    background: #f4f0ff;
                    color: var(--primary-dark);
                    border: 1px solid rgba(109, 78, 242, 0.1);
                    font-weight: 600;
                    font-size: 0.88rem;
                }

                .cards {
                    display: grid;
                    gap: 12px;
                }

                .product-card, .routine-card {
                    background: rgba(255,255,255,0.82);
                    border: 1px solid var(--line);
                    border-radius: 18px;
                    padding: 16px;
                }

                .product-top {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 12px;
                    margin-bottom: 8px;
                }

                .product-name {
                    font-weight: 800;
                    font-size: 1.05rem;
                }

                .score {
                    background: rgba(46, 169, 122, 0.1);
                    color: #1f7a5e;
                    border-radius: 999px;
                    padding: 6px 10px;
                    font-weight: 700;
                    font-size: 0.8rem;
                }

                .muted { color: var(--muted); }

                .routine-card {
                    display: grid;
                    gap: 4px;
                }

                .routine-time {
                    color: var(--primary-dark);
                    font-weight: 700;
                    font-size: 0.76rem;
                    text-transform: uppercase;
                    letter-spacing: 0.07em;
                }

                .analytics-grid {
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 12px;
                    margin-bottom: 16px;
                }

                .metric-card {
                    padding: 16px;
                    border-radius: 18px;
                    border: 1px solid var(--line);
                    background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(239, 232, 255, 0.7));
                }

                .metric-head {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    font-size: 0.82rem;
                    color: var(--muted);
                    margin-bottom: 10px;
                }

                .metric-value {
                    font-size: 1.7rem;
                    font-weight: 800;
                    letter-spacing: -0.04em;
                }

                .metric-trend {
                    margin-top: 8px;
                    font-size: 0.76rem;
                    color: var(--success);
                    font-weight: 700;
                }

                .progress-card {
                    border: 1px solid var(--line);
                    border-radius: 18px;
                    background: rgba(255,255,255,0.76);
                    padding: 16px;
                    margin-bottom: 18px;
                }

                .bars {
                    display: grid;
                    gap: 12px;
                    margin-top: 10px;
                }

                .bar-row {
                    display: grid;
                    grid-template-columns: 110px 1fr 36px;
                    align-items: center;
                    gap: 10px;
                    font-size: 0.82rem;
                    color: var(--muted);
                }

                .bar-track {
                    position: relative;
                    height: 10px;
                    border-radius: 999px;
                    background: #efeaf9;
                    overflow: hidden;
                }

                .bar-fill {
                    position: absolute;
                    inset: 0 auto 0 0;
                    border-radius: inherit;
                    background: linear-gradient(90deg, var(--primary), #ec4899);
                }

                .ring-row {
                    display: grid;
                    grid-template-columns: 120px 1fr;
                    gap: 18px;
                    align-items: center;
                    margin-top: 12px;
                }

                .ring {
                    --percent: 76;
                    width: 110px;
                    height: 110px;
                    border-radius: 50%;
                    background: conic-gradient(var(--primary) calc(var(--percent) * 1%), #f0eafc 0);
                    display: grid;
                    place-items: center;
                    position: relative;
                }

                .ring::before {
                    content: "";
                    position: absolute;
                    inset: 12px;
                    background: white;
                    border-radius: 50%;
                }

                .ring-score {
                    position: relative;
                    z-index: 1;
                    font-size: 1.2rem;
                    font-weight: 800;
                }

                .chart-days {
                    display: flex;
                    align-items: end;
                    justify-content: space-between;
                    gap: 10px;
                    height: 90px;
                    margin-top: 14px;
                }

                .day-col {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: end;
                    gap: 8px;
                    width: 100%;
                }

                .day-bar {
                    width: 100%;
                    max-width: 18px;
                    border-radius: 8px 8px 0 0;
                    background: linear-gradient(180deg, #c9b7ff, var(--primary));
                    min-height: 12px;
                }

                .day-label {
                    font-size: 0.7rem;
                    color: var(--muted);
                }

                @media (max-width: 900px) {
                    .hero, .content-grid { grid-template-columns: 1fr; }
                }

                @media (max-width: 540px) {
                    body { padding: 18px 12px 42px; }
                    .topbar { padding: 8px 12px; }
                    .hero-copy, .form-panel, .results-panel { padding: 20px 18px; }
                    .two-col, .analytics-grid { grid-template-columns: 1fr; }
                    .hero-stats { grid-template-columns: 1fr; }
                    .bar-row { grid-template-columns: 76px 1fr 30px; }
                    .ring-row { grid-template-columns: 1fr; }
                }
            </style>
        </head>
        <body>
            <div class="app-shell">
                <header class="topbar">
                    <div class="brand">
                        <div class="brand-mark">D</div>
                        <span>DermaTracker AI</span>
                    </div>
                    <div class="badge">Skin intelligence</div>
                </header>

                <section class="hero">
                    <div class="panel hero-copy">
                        <div class="badge">Smart dermatologist-style guidance</div>
                        <h1>Personalized skin care, built for your routine.</h1>
                        <p>
                            Analyze your concerns, track ingredient sensitivities, and get customized product picks and a practical daily routine
                            designed around your skin profile.
                        </p>
                        <div class="hero-stats">
                            <div class="stat">
                                <strong>4x</strong>
                                <span>Faster product matching</span>
                            </div>
                            <div class="stat">
                                <strong>90%</strong>
                                <span>Barrier-aware logic</span>
                            </div>
                            <div class="stat">
                                <strong>1-click</strong>
                                <span>Routine generation</span>
                            </div>
                        </div>
                    </div>

                    <div class="panel hero-demo">
                        <div class="mini-card">
                            <div class="label">Current concern</div>
                            <div class="value">Dry, irritated skin</div>
                        </div>
                        <div class="mini-card">
                            <div class="label">Recommended focus</div>
                            <div class="value">Hydration + barrier repair</div>
                        </div>
                        <div class="mini-card">
                            <div class="label">Routine style</div>
                            <div class="value">Minimal, fragrance-free, calming</div>
                        </div>
                    </div>
                </section>

                <section class="content-grid">
                    <div class="panel form-panel">
                        <h2>Skin profile</h2>
                        <form id="skin-form">
                            <div class="field">
                                <label for="user_message">Describe your skin</label>
                                <textarea id="user_message" placeholder="My skin gets flaky and irritated in winter, and I’m dealing with redness and dullness.">My skin gets flaky and irritated in winter, and I’m dealing with redness and dullness.</textarea>
                            </div>

                            <div class="two-col">
                                <div class="field">
                                    <label for="skin_type">Skin type</label>
                                    <select id="skin_type">
                                        <option value="">Select</option>
                                        <option value="dry">Dry</option>
                                        <option value="oily">Oily</option>
                                        <option value="balanced">Balanced</option>
                                        <option value="sensitive">Sensitive</option>
                                        <option value="combination">Combination</option>
                                    </select>
                                </div>

                                <div class="field">
                                    <label for="sensitivity_level">Sensitivity</label>
                                    <select id="sensitivity_level">
                                        <option value="">Select</option>
                                        <option value="low">Low</option>
                                        <option value="moderate">Moderate</option>
                                        <option value="high">High</option>
                                    </select>
                                </div>
                            </div>

                            <div class="two-col">
                                <div class="field">
                                    <label for="allergies">Allergies / avoid ingredients</label>
                                    <input id="allergies" value="fragrance" placeholder="fragrance, alcohol, salicylic acid" />
                                </div>

                                <div class="field">
                                    <label for="goals">Goals</label>
                                    <input id="goals" value="hydration, brightening" placeholder="hydration, acne control, glow" />
                                </div>
                            </div>

                            <button type="submit" class="submit-btn">Generate guidance</button>
                        </form>
                    </div>

                    <div class="panel results-panel">
                        <h2>AI recommendations</h2>
                        <div id="loading" class="loading">
                            <span class="spinner"></span>
                            <span>Analyzing your skin profile...</span>
                        </div>

                        <div id="results" class="result-wrap">
                            <div class="section-block">
                                <div class="section-head">
                                    <h3>Skin summary</h3>
                                </div>
                                <div id="summary"></div>
                            </div>

                            <div class="section-block">
                                <div class="section-head">
                                    <h3>Primary concerns</h3>
                                </div>
                                <div id="concerns" class="tag-list"></div>
                            </div>

                            <div class="section-block">
                                <div class="section-head">
                                    <h3>Report tracking</h3>
                                </div>
                                <div id="analytics"></div>
                            </div>

                            <div class="section-block">
                                <div class="section-head">
                                    <h3>Suggested products</h3>
                                </div>
                                <div id="products" class="cards"></div>
                            </div>

                            <div class="section-block">
                                <div class="section-head">
                                    <h3>Routine plan</h3>
                                </div>
                                <div id="routine" class="cards"></div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <script>
                const form = document.getElementById('skin-form');
                const loading = document.getElementById('loading');
                const results = document.getElementById('results');

                function parseList(value) {
                    return value.split(',').map((item) => item.trim()).filter(Boolean);
                }

                function renderTags(containerId, values) {
                    const container = document.getElementById(containerId);
                    container.innerHTML = '';

                    if (!values || values.length === 0) {
                        container.innerHTML = '<span class="muted">No data yet.</span>';
                        return;
                    }

                    values.forEach((value) => {
                        const tag = document.createElement('span');
                        tag.className = 'tag';
                        tag.textContent = value;
                        container.appendChild(tag);
                    });
                }

                function computeMetrics(analysis, products) {
                    const concernSet = new Set((analysis.primary_concerns || []).map((item) => item.toLowerCase()));
                    const averageScore = products.length ? products.reduce((sum, item) => sum + (Number(item.score) || 0), 0) / products.length : 76;

                    const hydration = concernSet.has('dryness') ? 84 : 72;
                    const barrier = concernSet.has('sensitivity') || concernSet.has('barrier repair') ? 81 : 74;
                    const clarity = concernSet.has('acne') || concernSet.has('texture') || concernSet.has('hyperpigmentation') ? 78 : 70;
                    const adherence = concernSet.has('sensitivity') ? 79 : 82;

                    const score = Math.min(100, Math.round((averageScore + hydration + barrier + clarity + adherence) / 5));

                    return {
                        hydration: Math.max(55, Math.min(96, hydration)),
                        barrier: Math.max(58, Math.min(96, barrier)),
                        clarity: Math.max(60, Math.min(94, clarity)),
                        adherence: Math.max(60, Math.min(95, adherence)),
                        progress: score,
                    };
                }

                function renderAnalytics(analysis, products) {
                    const container = document.getElementById('analytics');
                    const metrics = computeMetrics(analysis, products);
                    const score = metrics.progress;

                    const bars = [
                        { name: 'Hydration', value: metrics.hydration },
                        { name: 'Barrier', value: metrics.barrier },
                        { name: 'Clarity', value: metrics.clarity },
                        { name: 'Adherence', value: metrics.adherence },
                    ];

                    const days = [
                        { label: 'Mon', value: 58 },
                        { label: 'Tue', value: 64 },
                        { label: 'Wed', value: 68 },
                        { label: 'Thu', value: 74 },
                        { label: 'Fri', value: 79 },
                        { label: 'Sat', value: 82 },
                        { label: 'Sun', value: score },
                    ];

                    container.innerHTML = `
                        <div class="analytics-grid">
                            <div class="metric-card">
                                <div class="metric-head">
                                    <span>Hydration</span>
                                    <span>+6%</span>
                                </div>
                                <div class="metric-value">${metrics.hydration}%</div>
                                <div class="metric-trend">Improving this week</div>
                            </div>
                            <div class="metric-card">
                                <div class="metric-head">
                                    <span>Barrier</span>
                                    <span>+8%</span>
                                </div>
                                <div class="metric-value">${metrics.barrier}%</div>
                                <div class="metric-trend">Less irritation</div>
                            </div>
                            <div class="metric-card">
                                <div class="metric-head">
                                    <span>Clarity</span>
                                    <span>+4%</span>
                                </div>
                                <div class="metric-value">${metrics.clarity}%</div>
                                <div class="metric-trend">Texture is settling</div>
                            </div>
                            <div class="metric-card">
                                <div class="metric-head">
                                    <span>Routine</span>
                                    <span>+9%</span>
                                </div>
                                <div class="metric-value">${metrics.adherence}%</div>
                                <div class="metric-trend">Consistency rising</div>
                            </div>
                        </div>

                        <div class="progress-card">
                            <div class="section-head">
                                <h3>Skin score</h3>
                            </div>
                            <div class="ring-row">
                                <div class="ring" style="--percent:${score};">
                                    <div class="ring-score">${score}%</div>
                                </div>
                                <div>
                                    <div class="muted">Progress snapshot</div>
                                    <div style="margin-top:8px; font-weight:800; font-size:1.1rem;">Your routine is trending in the right direction.</div>
                                    <div style="margin-top:8px; color: var(--muted); line-height:1.6;">
                                        Maintain gentle hydration and continue barrier support to reduce sensitivity flare-ups.
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="progress-card">
                            <div class="section-head">
                                <h3>Goal tracking</h3>
                            </div>
                            <div class="bars">
                                ${bars.map((bar) => `
                                    <div class="bar-row">
                                        <span>${bar.name}</span>
                                        <div class="bar-track">
                                            <div class="bar-fill" style="width:${bar.value}%"></div>
                                        </div>
                                        <strong>${bar.value}%</strong>
                                    </div>
                                `).join('')}
                            </div>
                        </div>

                        <div class="progress-card">
                            <div class="section-head">
                                <h3>7-day routine adherence</h3>
                            </div>
                            <div class="chart-days">
                                ${days.map((item) => `
                                    <div class="day-col">
                                        <div class="day-bar" style="height:${item.value}%"></div>
                                        <div class="day-label">${item.label}</div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `;
                }

                function renderProducts(items) {
                    const container = document.getElementById('products');
                    if (!items || !items.length) {
                        container.innerHTML = '<div class="muted">No products matched your current skin profile.</div>';
                        return;
                    }

                    container.innerHTML = items.map((item) => `
                        <div class="product-card">
                            <div class="product-top">
                                <div class="product-name">${item.name}</div>
                                <div class="score">${item.score}</div>
                            </div>
                            <div class="muted">${item.category}</div>
                            <p>${item.rationale}</p>
                            <div class="tag-list">
                                ${(item.ingredients || []).slice(0, 4).map((ingredient) => `<span class="tag">${ingredient}</span>`).join('')}
                            </div>
                        </div>
                    `).join('');
                }

                function renderRoutine(items) {
                    const container = document.getElementById('routine');
                    if (!items || !items.length) {
                        container.innerHTML = '<div class="muted">No routine available yet.</div>';
                        return;
                    }

                    container.innerHTML = items.map((item) => `
                        <div class="routine-card">
                            <div class="routine-time">${item.time_of_day}</div>
                            <div class="product-name">${item.step}</div>
                            <div class="muted">${item.purpose}</div>
                        </div>
                    `).join('');
                }

                form.addEventListener('submit', async (event) => {
                    event.preventDefault();

                    const payload = {
                        user_message: document.getElementById('user_message').value,
                        skin_type: document.getElementById('skin_type').value || null,
                        allergies: parseList(document.getElementById('allergies').value),
                        goals: parseList(document.getElementById('goals').value),
                        sensitivity_level: document.getElementById('sensitivity_level').value || null,
                        current_products: [],
                        current_issues: [],
                        climate: 'moderate',
                    };

                    loading.classList.add('visible');
                    results.classList.remove('visible');

                    try {
                        const response = await fetch('/recommendation', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload),
                        });

                        if (!response.ok) throw new Error('Unable to generate recommendations');

                        const data = await response.json();
                        const analysis = data.analysis || {};

                        document.getElementById('summary').textContent = analysis.summary || 'No summary generated yet.';
                        renderTags('concerns', analysis.primary_concerns || []);
                        renderAnalytics(analysis, data.products || []);
                        renderProducts(data.products || []);
                        renderRoutine(data.routine || []);

                        loading.classList.remove('visible');
                        results.classList.add('visible');
                    } catch (error) {
                        loading.classList.remove('visible');
                        document.getElementById('summary').textContent = error.message || 'Something went wrong.';
                        renderTags('concerns', []);
                        renderAnalytics({ primary_concerns: ['dryness'] }, []);
                        renderProducts([]);
                        renderRoutine([]);
                        results.classList.add('visible');
                    }
                });

                window.addEventListener('DOMContentLoaded', () => {
                    form.dispatchEvent(new Event('submit'));
                });
            </script>
        </body>
        </html>
        """
    )


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "derma-tracker-ai"}


@app.post("/recommendation")
def recommendation(query: SkinQuery):
    return service.generate_recommendations(query)

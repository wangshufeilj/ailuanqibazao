#!/usr/bin/env python3
"""
批量目录细分与文件迁移脚本
- reading/notes/politics -> 5个议题子目录
- reading/notes/technology -> 5个产业子目录
- generated/summaries -> 4个主题子目录
支持重编号和 frontmatter category 字段更新
"""

from pathlib import Path
import re
import shutil

REPO_ROOT = Path("d:/AI驱动整理乱七八糟")

# ===== 映射定义（原始三位序号 -> 目标子目录） =====

POLITICS_SUBDIR = {
    1: "conflict-security",    # Six-Arrested-Explosive-Mamdani
    2: "conflict-security",    # US-Iran-Conflict
    3: "geo-politics",         # US-Gulf-Bases-Hungary-Ukraine-RT
    4: "domestic-policy",      # Russian-Defense-Ministry-Graft
    5: "geo-politics",         # US-Gulf-Bases-Hungary-Ukraine-Part1
    6: "geo-politics",         # US-Gulf-Bases-Hungary-Ukraine-Part2
    7: "domestic-policy",      # Trump-Florsheim-Shoe-Lawsuit
    8: "domestic-policy",      # Trump-Florsheim-Shoes-Gift
    9: "domestic-policy",      # Osaka-Steel-Pipe-Uplift-Engineering
    10: "domestic-policy",     # GOP-Georgia-Special-Election
    11: "conflict-security",   # Italy-US-Airbase-Drone-Attack
    12: "domestic-policy",     # Quarry-Boss-Danny-Guerra
    13: "diplomacy",           # 中文外交指引
    14: "domestic-policy",     # Joseph-Kent-NCTC-Resignation
    15: "conflict-security",   # US-Israeli-Strike-Iran-South-Pars
    16: "geo-politics",        # 台湾历史相关
    17: "domestic-policy",     # 中文某条
    18: "geo-politics",        # 中文某条（两岸/春节）
    19: "geo-politics",        # 中美贸易谈判
    20: "domestic-policy",     # 中国规范
    21: "diplomacy",           # 越南外交3月战后
    22: "domestic-policy",     # 浙江省委
    23: "domestic-policy",     # 某第一次
    24: "conflict-security",   # US-F-35-Emergency-Landing-Iran
    25: "domestic-policy",     # US-refinery-fire
    26: "domestic-policy",     # 中国渔业协会
    27: "domestic-policy",     # China-Investing-in-People
    28: "domestic-policy",     # Two-Fox-Reporters-Congressmen
    29: "geo-politics",        # Iran-Barbarian-Invasion-Cultural-Heritage
    30: "geo-politics",        # US-Names-Five-Countries-Security-Threats
    31: "diplomacy",           # Takaichi-US-Dinner-Photo
    32: "domestic-policy",     # Cockroaches-Will-Be-Watching-Us (Russia)
    33: "conflict-security",   # How-Iranian-Air-Defense-Hit-F-35
    34: "domestic-policy",     # Novosibirsk-Heating-Network-Accident
    35: "geo-politics",        # Closed-Border-with-Finland
    36: "domestic-policy",     # Davignon-Lumumba-Belgium-Trial
    37: "diplomacy",           # Li-highlights-fair-trade-CDF
    38: "geo-politics",        # China-More-Dependable-Partner
    39: "geo-politics",        # Heixiazi-Island-Checkpoint
    40: "diplomacy",           # KPRF-Delegation-Soong-Residence
    41: "domestic-policy",     # KPRF-Udmurt-Ionov-Obituary
    42: "domestic-policy",     # Kucharov-Namaz-Hero-Uzbek
    43: "domestic-policy",     # Trump-Conqueror-of-Iran
    44: "domestic-policy",     # Trump-Mental-Health-Debate
    45: "domestic-policy",     # Trump-Second-Term-Speech-Patterns
    46: "domestic-policy",     # Health-Competence-Trump-Predecessors
    47: "domestic-policy",     # Most-Say-Trump-Becoming-More-Erratic
    48: "domestic-policy",     # Trump-Regime-Psychiatric
    49: "domestic-policy",     # Putin-National-Guard-Day
    50: "domestic-policy",     # Trump-New-Science-Panel-PCAST
    51: "domestic-policy",     # Trump-Signature-US-100-Dollar-Bill
    52: "energy-sanctions",    # Russia-Presidential-Decree-193-Cash-Gold
    53: "domestic-policy",     # Zhambyl-Presidential-Residence-Governor
    54: "domestic-policy",     # Rubio-State-Department-Restructuring
    55: "diplomacy",           # Iran-Pezeshkian-EU-Costa-Phone
    56: "geo-politics",        # US-Busy-Iran-War-China-DRC-Minerals
    57: "diplomacy",           # Israel-Stops-Security-Purchases-France
    58: "conflict-security",   # Nigeria-Plateau-State-University-Attack
    59: "domestic-policy",     # Army-Reaffirms-Ban-Camouflage (Nigeria)
    60: "domestic-policy",     # Nigeria-ONSA-Camouflage
    61: "domestic-policy",     # Nigeria-MoD-Matawalle
    62: "conflict-security",   # Somali-Army-Baidoa
    63: "energy-sanctions",    # Russian-Oil-Tanker-Cuba-VnExpress
    64: "domestic-policy",     # Russia-Hotel-Check-In-Driver-License
    65: "energy-sanctions",    # Russia-Oil-Tanker-Cuba-RT
    66: "energy-sanctions",    # Russian-Tanker-Cuba-Le-Monde
    67: "energy-sanctions",    # Russian-Oil-Tanker-Cuba-US-Embargo
    68: "energy-sanctions",    # Russian-Oil-Tanker-Matanzas-Cuba-Reuters
    69: "geo-politics",        # US-Embassies-Counter-Hostile-Propaganda
    70: "domestic-policy",     # CBE-Remote-Work-Egyptian-Banks
    71: "geo-politics",        # Egypt-Europe-Gulf-RoRo-Damietta
    72: "domestic-policy",     # Egypt-Ashraf-Zaher-Defense-Minister
    73: "diplomacy",           # Turkey-Egypt-Military-Framework
    74: "energy-sanctions",    # Hungary-Ukraine-Gas-Suspend-Druzhba
    75: "conflict-security",   # US-Israel-Iran-Military-Operation-Chronicle
    76: "energy-sanctions",    # Russia-Gasoline-Export-Ban
    77: "conflict-security",   # US-Israel-Iran-One-Month-War-Key-Nodes
    78: "geo-politics",        # Russia-Eastern-Polygon-BAM-Trans-Siberian
    79: "geo-politics",        # Japan-Long-Range-Missile-Deployment
    80: "geo-politics",        # Taiwan-Oil-Shortage-TAO-Peaceful-Unification
    81: "diplomacy",           # Wang-Yi-Dar-Pakistan-China-Five-Point
    82: "diplomacy",           # SDF-Officer-Chinese-Embassy-Intrusion
    83: "geo-politics",        # Persistent-Yen-Depreciation-Japan-Economy
    84: "diplomacy",           # Pezeshkian-Open-Letter-US
    85: "geo-politics",        # NSR-Year-Round-Navigation-EastRussia
    86: "conflict-security",   # US-E3-Sentry-AWACS-Destroyed-Saudi-Arabia
}

TECHNOLOGY_SUBDIR = {
    1:  "ai-digital",          # Cursor-Models-Pricing
    2:  "industry-policy",     # 2026-Global-Petroleum-Petrochemical
    3:  "industry-policy",     # China-Sci-Tech-Innovation
    4:  "industry-policy",     # 科技创新发展硬实力
    5:  "industry-policy",     # 氢能新一轮源
    6:  "industry-policy",     # 技术能力水平
    7:  "industry-policy",     # 俄罗斯工业新兴产业
    8:  "industry-policy",     # 合成实验（硬件实验）
    9:  "automotive",          # 巅峰比较-Supercar-Blondie-小米SU7
    10: "automotive",          # NIO-Neo-Park-Factory-Tour
    11: "industry-policy",     # 工业稳定经济
    12: "semiconductor",       # Reuters-China-No2-Chipmaker-7nm
    13: "semiconductor",       # Hua-Hong-Semiconductor
    14: "industry-policy",     # 科技2019裙摆
    15: "ai-digital",          # State-of-Reasoning-LLMs
    16: "ai-digital",          # Reasoning-LLMs-Glossary
    17: "ai-digital",          # Reasoning-Optimized-LLMs-Survey
    18: "ai-digital",          # 知识图谱-推理模型
    19: "ai-digital",          # Jina-AI-30M-Series-A
    20: "ai-digital",          # Jina-AI-业务
    21: "industry-policy",     # WSJ-Tech-Industry-Huge-Europe-Share
    22: "ai-digital",          # China-Tech-Trial-Space-Computing-Humanoid
    23: "industry-policy",     # 价格调整
    24: "industry-policy",     # 清华大学500亩医学院
    25: "ai-digital",          # Complete-Guide-Tech-Marketing-Buzzwords
    26: "ai-digital",          # 2000s-Tech-Marketing-Buzzwords
    27: "ai-digital",          # Early-Mid-2010s-Disruption-IoT
    28: "ai-digital",          # Late-2010s-to-2020s-Blockchain-Metaverse
    29: "automotive",          # 上海中低档价格战
    30: "ai-digital",          # NYT-10-Tech-Jargon-Confused-Us
    31: "ai-digital",          # How-to-Speak-Silicon-Valley
    32: "automotive",          # BYD-Lawsuit-Trump-US-Auto-Tariffs (两版)
    33: "automotive",          # BYD-unveils-North-Americas-electric-bus
    34: "ai-digital",          # Markdownify-MCP-Skills
    35: "shipping-logistics",  # RIDE-Apprenticeship-Program
    36: "shipping-logistics",  # RIDE-Pre-Apprenticeship
    37: "shipping-logistics",  # RIDE-Love-the-Bus-Month
    38: "automotive",          # A-Tour-of-BYD-Factory-Lancaster
    39: "industry-policy",     # Explore-Top-Tech-Companies-California
    40: "ai-digital",          # Cursor-Composer-2-Kimi-K2.5
    41: "ai-digital",          # Composer-Building-Fast-Frontier
    42: "ai-digital",          # Introduction-to-Frontend-Development
    43: "ai-digital",          # Reddit-Sues-Perplexity
    44: "ai-digital",          # Cloudflare-416-Billion-AI-Bot
    45: "ai-digital",          # Cloudflare-Permission-Based-AI-Crawlers
    46: "industry-policy",     # CBS-News-Radio-Shuttering
    47: "shipping-logistics",  # China-Intensifies-Inspections-Panamanian
    48: "ai-digital",          # How-AI-Is-Reshaping-China-Manufacturing
    49: "ai-digital",          # AI-Boom-Value-Anchor
    50: "industry-policy",     # Blagoveshchensk-Three-Gas-Boiler
    51: "ai-digital",          # Xinhua-Seedance-2-Hollywood
    52: "industry-policy",     # Laser-Die-Cutting-Bakers-Dozen
    53: "automotive",          # BELTA-Electric-Buses-Belarus
    54: "automotive",          # BELTA-Personal-Mobility-Lithium-Battery
    55: "shipping-logistics",  # Almaty-Bishkek-Highway-8-Lanes
    56: "industry-policy",     # 24KZ-Karaganda-Grid-Aktobe
    57: "shipping-logistics",  # 24KZ-Kostanay-Housing-Zhambyl-Highway
    58: "automotive",          # Brazil-Dual-Fuel-Ethanol-Fleet
    59: "industry-policy",     # Amazon-16000-Layoffs
    60: "industry-policy",     # BI-Companies-Laying-Off
    61: "industry-policy",     # Oracle-USA-TODAY-AI-Layoffs
    62: "industry-policy",     # Kiwi-Ears-Cadenza
    63: "industry-policy",     # Honor-360W-GaN-Samsung-Wine
    64: "automotive",          # Moskvich-Umo-EV-Plant
    65: "industry-policy",     # Unnamed-Chinese-Brand-Triple-200MP
    66: "semiconductor",       # Chinese-Chipmakers-Market-Share-Nvidia
    67: "shipping-logistics",  # World-First-10000-Unit-Dual-Fuel-PCTC
    68: "automotive",          # China-Cars-Overtake-Japan
    69: "industry-policy",     # Seeing-2030-15th-FYP-Smart-Agriculture
}

# generated/summaries 原始序号 -> 子目录
SUMMARIES_SUBDIR = {
    1:  "politics",    # US-Military-Bases-Middle-East-Map
    2:  "other",       # City-Rooftops-Dramatic-Sky
    3:  "other",       # m2-Res-1280p
    6:  "politics",    # Daily-Telegraph-Starmer-US-Iran
    7:  "other",       # City-Skyline-Smoke-Sunset
    8:  "science",     # Mandrill-Wildlife-Photo
    9:  "science",     # Cosmic-Web-Structure-Visualization
    10: "science",     # Green-Crab-Shallow-Water
    11: "science",     # Spiny-Lobster-Coral-Reef
    12: "science",     # Colorful-Crab-Rocky-Shore
    13: "politics",    # US-China-Research-Publications
    14: "other",       # PEDHA-BS-Degrees-Reported
    15: "other",       # Globe-Motors-Component-OSINT
    16: "politics",    # ESA-Sentinel-2-Kharg-Island-Iran
    17: "technology",  # AI-Buzzword-Bingo-Meeting-Satire
    18: "technology",  # KPPU-AUX-Distribution-Hearing
    19: "other",       # Star-Trek-Starships-Collection
    20: "politics",    # WHCA-Fitzpatrick-Heinrich-Red-Carpet
    21: "politics",    # Institutional-Building-Federal-Case
    22: "technology",  # Century-of-Fighter-Jets-Book-Cover
    23: "politics",    # Ballistic-Missile-Vertical-Launch
    24: "politics",    # Chinese-Calligraphy-Integrity-Quote-Poster
    25: "other",       # bridge-tower-picture-set
    26: "other",       # Moskvich-Polyarnik-Snow-Mountains-BAM
    27: "other",       # Moskvich-Polyarnik-Birobidzhan-Night
    28: "other",       # Moskvich-Polyarnik-Vostochny-Cosmodrome
    29: "politics",    # KPRF-Beijing-outdoor-delegation-visit
    30: "politics",    # KPRF-Beijing-museum-exhibit-briefing
    31: "politics",    # KPRF-Beijing-Zhostovo-tray-gift
    32: "politics",    # KPRF-Beijing-guestbook-CPC-exhibit
    33: "politics",    # KPRF-Beijing-delegation-group-photo
    34: "politics",    # KPRF-Beijing-Soong-residence-tea-meeting
    35: "technology",  # Golden-Laser-Industrial-Visit-OSINT
    36: "politics",    # US-100-Dollar-Trump-Signature-Image
    37: "politics",    # Trump-Commemorative-Coin-TV-Screenshot
    38: "other",       # Renwu-Li-Yunxiao-March-2026-Cover-Bronze
    39: "other",       # Renwu-Li-Yunxiao-March-2026-Cover-Outdoor
    40: "politics",    # Russian-Tanker-Anatoliy-Kolodkin-Cuba-AFP
    41: "politics",    # Russian-Tanker-Anatoliy-Kolodkin-Cuba-Reuters
    42: "politics",    # Pakistan-Egypt-Saudi-Turkey-Islamabad-FM
    43: "technology",  # 15th-Five-Year-Plan-Young-Drafters-Video
    44: "politics",    # RYBAR-Middle-East-Instability
    45: "technology",  # Zhonghua-Kao-Gong-Ji-Season-1-Poster
    46: "politics",    # Raid-Al-Mutairi-Liaoning-Friendship-Award
    47: "politics",    # China-Pipeline-Gas-Network-Power-of-Siberia
    48: "politics",    # China-Natural-Gas-Consumption-Sources
    49: "politics",    # China-Electricity-Share-by-Source
    50: "politics",    # China-EV-Oil-Displacement-IEA-CREA
    51: "politics",    # China-Embassy-Female-Diplomats-VK-Meeting
    52: "politics",    # China-Embassy-Female-Diplomats-VK-Group-Tour
}


def extract_num(filename: str) -> int | None:
    """从文件名提取前导序号"""
    m = re.match(r'^(\d{3})', filename)
    return int(m.group(1)) if m else None


def replace_leading_num(filename: str, new_num: int) -> str:
    """将文件名前导序号替换为新序号"""
    return re.sub(r'^\d{3}', f'{new_num:03d}', filename)


def update_category_frontmatter(file_path: Path, new_category: str) -> bool:
    """更新 YAML frontmatter 中的 category 字段；返回是否有修改"""
    text = file_path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return False
    # 找到 frontmatter 结束位置
    end = text.find('\n---', 3)
    if end == -1:
        return False
    frontmatter = text[:end + 4]
    rest = text[end + 4:]
    new_fm = re.sub(
        r'^(category:\s*).*$',
        f'\\g<1>{new_category}',
        frontmatter,
        flags=re.MULTILINE
    )
    if new_fm == frontmatter:
        return False
    file_path.write_text(new_fm + rest, encoding='utf-8')
    return True


def migrate_directory(
    src_dir: Path,
    subdir_map: dict,
    base_category: str,
    migration_log: list,
):
    """
    迁移一个扁平目录到按议题细分的子目录。
    src_dir: 源目录（读取其中所有 *.md 文件）
    subdir_map: {原始序号(int) -> 子目录名(str)}
    base_category: 新 category 路径前缀（如 reading/notes/politics）
    migration_log: 追加迁移记录
    """
    files = sorted(src_dir.glob('*.md'))
    # 建立 num -> file 映射
    num_to_file: dict[int, list[Path]] = {}
    unmapped = []
    for f in files:
        num = extract_num(f.name)
        if num is None or num not in subdir_map:
            unmapped.append(f.name)
            continue
        num_to_file.setdefault(num, []).append(f)

    if unmapped:
        print(f"  [WARN] 未映射文件（跳过）: {unmapped}")

    # 按子目录收集，保持原始序号顺序
    subdir_groups: dict[str, list[tuple[int, Path]]] = {}
    for num in sorted(num_to_file.keys()):
        for f in sorted(num_to_file[num]):  # 同号多文件（如 032 两版）
            sd = subdir_map[num]
            subdir_groups.setdefault(sd, []).append((num, f))

    # 迁移
    for sd_name, items in subdir_groups.items():
        target_dir = src_dir / sd_name
        target_dir.mkdir(exist_ok=True)
        # 放一个 .gitkeep 占位（如果目录为空还没文件时）
        for new_num, (orig_num, src_file) in enumerate(items, start=1):
            new_name = replace_leading_num(src_file.name, new_num)
            dst_file = target_dir / new_name
            shutil.move(str(src_file), str(dst_file))
            new_category = f"{base_category}/{sd_name}"
            changed = update_category_frontmatter(dst_file, new_category)
            migration_log.append({
                'old': str(src_file.relative_to(REPO_ROOT)),
                'new': str(dst_file.relative_to(REPO_ROOT)),
                'category_updated': changed,
            })
            print(f"  {orig_num:03d}->{new_num:03d} [{sd_name}] {src_file.name[:60]}")


def fix_military_photos_duplicates():
    """修复 images/photos/military/ 中两个 001- 文件的编号冲突"""
    mil_dir = REPO_ROOT / "images/photos/military"
    files = sorted(mil_dir.glob("*.md"))
    nums: dict[int, list[Path]] = {}
    for f in files:
        n = extract_num(f.name)
        if n is not None:
            nums.setdefault(n, []).append(f)
    # 找到重复的序号
    for n, flist in nums.items():
        if len(flist) > 1:
            print(f"  修复 military/ 重复序号 {n:03d}:")
            # 按文件名字母排序，第一个保留，后续重新编号
            flist_sorted = sorted(flist)
            max_existing = max(extract_num(f.name) for f in files)
            for extra in flist_sorted[1:]:
                max_existing += 1
                new_name = replace_leading_num(extra.name, max_existing)
                new_path = extra.parent / new_name
                shutil.move(str(extra), str(new_path))
                print(f"    {extra.name} -> {new_name}")


def main():
    print("=" * 60)
    print("目录细分迁移脚本")
    print("=" * 60)
    migration_log = []

    # 1. 创建目标子目录骨架（提前创建，避免 move 失败）
    politics_dir = REPO_ROOT / "reading/notes/politics"
    tech_dir = REPO_ROOT / "reading/notes/technology"
    summaries_dir = REPO_ROOT / "generated/summaries"

    for sd in ["geo-politics", "diplomacy", "conflict-security", "energy-sanctions", "domestic-policy"]:
        (politics_dir / sd).mkdir(exist_ok=True)
    for sd in ["semiconductor", "automotive", "shipping-logistics", "ai-digital", "industry-policy"]:
        (tech_dir / sd).mkdir(exist_ok=True)
    for sd in ["politics", "technology", "science", "other"]:
        (summaries_dir / sd).mkdir(exist_ok=True)

    print("\n[1/4] 迁移 reading/notes/politics/")
    migrate_directory(politics_dir, POLITICS_SUBDIR, "reading/notes/politics", migration_log)

    print("\n[2/4] 迁移 reading/notes/technology/")
    migrate_directory(tech_dir, TECHNOLOGY_SUBDIR, "reading/notes/technology", migration_log)

    print("\n[3/4] 迁移 generated/summaries/")
    migrate_directory(summaries_dir, SUMMARIES_SUBDIR, "generated/summaries", migration_log)

    print("\n[4/4] 修复 images/photos/military/ 重复编号")
    fix_military_photos_duplicates()

    # 输出迁移映射报告
    print("\n" + "=" * 60)
    print(f"迁移完成：共迁移 {len(migration_log)} 个文件")
    category_updated = sum(1 for r in migration_log if r['category_updated'])
    print(f"frontmatter category 字段已更新：{category_updated} 个文件")
    print("=" * 60)

    # 写入映射清单
    report_path = REPO_ROOT / "generated/migration-report-2026-04-04.txt"
    lines = ["旧路径 -> 新路径\n"]
    for r in migration_log:
        lines.append(f"{r['old']}\n  -> {r['new']}\n")
    report_path.write_text("".join(lines), encoding='utf-8')
    print(f"迁移映射清单已写入: {report_path.name}")


if __name__ == "__main__":
    main()

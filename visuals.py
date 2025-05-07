import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import networkx as nx
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import Rectangle, Circle, Arrow, Polygon
import matplotlib.colors as mcolors
import matplotlib.patheffects as path_effects
import datetime

# Set consistent styling for all visualizations
plt.style.use('seaborn-v0_8-whitegrid')
colors = sns.color_palette("viridis", 8)
accent_colors = sns.color_palette("Set2", 8)

# Slide 2: Iceberg Diagram of Microaggressions
def create_iceberg_diagram():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Water level
    ax.axhspan(0, 10, facecolor='lightblue', alpha=0.5)
    
    # Iceberg
    iceberg_x = np.array([2, 4, 6, 8, 10, 11, 9, 8, 7, 5, 2])
    iceberg_y_above = np.array([0, 0.5, 0, 1, 0, -1, 0, -0.5, -1, 0, 0])
    iceberg_y_below = np.array([0, -2, -4, -5, -8, -9, -7, -6, -4, -3, 0])
    
    ax.fill(iceberg_x, iceberg_y_above, color='white', edgecolor='black', alpha=0.9)
    ax.fill(iceberg_x, iceberg_y_below, color='lightblue', edgecolor='black', alpha=0.7)
    
    # Text for visible discrimination
    ax.text(6, 0.8, "VISIBLE DISCRIMINATION", fontsize=14, fontweight='bold', ha='center')
    ax.text(6, 0.3, "- Explicit racism, sexism, ableism\n- Open hostility\n- Conscious bias\n- Harassment", 
            fontsize=10, ha='center')
    
    # Text for microaggressions
    ax.text(6, -3, "MICROAGGRESSIONS", fontsize=14, fontweight='bold', ha='center')
    ax.text(6, -5, "- Subtle comments\n- Unconscious biases\n- Environmental slights\n- Exclusionary practices\n- Invalidating experiences", 
            fontsize=10, ha='center')
    
    # Waterline label
    ax.text(1, 0.1, "Surface Level", fontsize=12, ha='left', va='bottom')
    
    # Remove axes
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('iceberg_microaggressions.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "iceberg_microaggressions.png"

# Slide 3: Three-column chart of microaggression types
def create_microaggression_types_chart():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # Create three columns
    column_width = 0.3
    column_positions = [0.16, 0.5, 0.84]
    column_titles = ["MICROASSAULTS", "MICROINSULTS", "MICROINVALIDATIONS"]
    column_colors = [accent_colors[0], accent_colors[1], accent_colors[2]]
    column_descriptions = [
        "Explicit, intentional\ndiscriminatory actions",
        "Subtle rudeness or insensitivity\nthat demeans identity",
        "Comments that nullify the\nexperiences of marginalized groups"
    ]
    column_examples = [
        "• Using offensive slurs\n• Deliberately ignoring colleagues\n• Explicit stereotyping\n• Displaying offensive symbols\n• Exclusionary behaviors",
        "• \"You're so articulate\"\n• \"Where are you really from?\"\n• Avoiding certain colleagues\n• \"You don't look disabled\"\n• Assuming incompetence",
        "• \"I don't see color\"\n• \"Everyone can succeed if they try\"\n• \"It was just a joke\"\n• \"You're being too sensitive\"\n• \"We're all one human race\""
    ]
    
    for i, (pos, title, color, desc, examples) in enumerate(zip(
        column_positions, column_titles, column_colors, column_descriptions, column_examples)):
        
        # Draw column background
        rect = Rectangle((pos-column_width/2, 0.2), column_width, 0.7, 
                         facecolor=color, alpha=0.2, edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        
        # Add title
        ax.text(pos, 0.9, title, fontsize=14, fontweight='bold', ha='center')
        
        # Add description
        ax.text(pos, 0.8, desc, fontsize=12, ha='center', va='center', style='italic')
        
        # Line separator
        ax.plot([pos-column_width/2+0.02, pos+column_width/2-0.02], [0.75, 0.75], 
                color=color, linestyle='-', linewidth=2)
        
        # Add examples
        ax.text(pos, 0.53, examples, fontsize=11, ha='center', va='center')
    
    # Add title
    fig.suptitle('Types of Microaggressions in the Workplace', fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('microaggression_types.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "microaggression_types.png"

# Slide 4: Timeline of microaggression research
def create_research_timeline():
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Timeline settings
    start_year = 1970
    end_year = 2025
    years = list(range(start_year, end_year+1, 10))
    years[-1] = 2025
    
    # Draw timeline
    ax.plot([start_year, end_year], [0, 0], 'k-', linewidth=2)
    
    # Add ticks for decades
    for year in years:
        ax.plot([year, year], [-0.1, 0.1], 'k-', linewidth=2)
        ax.text(year, -0.3, str(year), ha='center')
    
    # Key events on timeline
    events = [
        (1970, 0.5, "Dr. Chester Pierce\ncoins term 'microaggression'\nfocusing on racial experiences", accent_colors[0]),
        (1986, -0.5, "Early studies on 'everyday racism'\nby Philomena Essed", accent_colors[1]),
        (2007, 0.5, "Dr. Derald Wing Sue expands concept\nto include all marginalized identities", accent_colors[2]),
        (2010, -0.5, "Research expands into workplace\nand organizational contexts", accent_colors[3]),
        (2015, 0.5, "Increased focus on intersectionality\nand multiple identity dimensions", accent_colors[4]),
        (2020, -0.5, "Growth in research on intervention\nand response strategies", accent_colors[5]),
        (2025, 0.5, "Current understanding incorporates\nintersectionality, contextual factors,\nand organizational impact", accent_colors[6])
    ]
    
    for year, pos, text, color in events:
        # Event dot
        ax.scatter(year, 0, s=100, color=color, zorder=5, edgecolor='black')
        
        # Line connecting to text
        ax.plot([year, year], [0, pos], color=color, linestyle='-', linewidth=1.5)
        
        # Event text with background
        text_box = ax.text(year, pos, text, ha='center', va='center', fontsize=9,
                   bbox=dict(facecolor='white', alpha=0.7, edgecolor=color, boxstyle='round,pad=0.5'))
        text_box.set_path_effects([path_effects.withStroke(linewidth=5, foreground='white')])
    
    # Remove axes
    ax.set_ylim(-1, 1)
    ax.set_xlim(start_year-5, end_year+5)
    ax.axis('off')
    
    # Title
    fig.suptitle('Evolution of Microaggression Research', fontsize=16, fontweight='bold', y=0.95)
    
    plt.tight_layout()
    plt.savefig('microaggression_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "microaggression_timeline.png"

# Slide 5: Infographic showing ripple effects of microaggressions
def create_ripple_effect_infographic():
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Create circular ripples
    center = (5, 5)
    ripple_radii = [1, 2, 3, 4]
    ripple_labels = ["MICROAGGRESSION\nEVENT", "INDIVIDUAL\nIMPACT", "TEAM\nEFFECT", "ORGANIZATIONAL\nCONSEQUENCES"]
    ripple_colors = [colors[i] for i in [0, 2, 4, 6]]
    
    for radius, label, color in zip(ripple_radii, ripple_labels, ripple_colors):
        circle = plt.Circle(center, radius, fill=True, alpha=0.2, color=color, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        if radius == 1:
            ax.text(center[0], center[1], label, ha='center', va='center', fontsize=10, fontweight='bold')
        else:
            # Place text at top of circle
            text_x = center[0]
            text_y = center[1] + radius - 0.2
            ax.text(text_x, text_y, label, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Add impact bullet points
    impacts = [
        # Ring 2 - Individual
        (4.5, 3.8, "• Psychological stress\n• Decreased engagement\n• Reduced confidence", 1),
        
        # Ring 3 - Team
        (3.0, 5.5, "• Communication barriers\n• Reduced collaboration\n• Loss of diverse perspectives", 2),
        (7.0, 4.5, "• Lower psychological safety\n• Strained relationships\n• Limited idea sharing", 2),
        
        # Ring 4 - Organization
        (2.0, 7.0, "• $15-30K turnover cost\n  per employee", 3),
        (5.0, 8.5, "• 15% productivity loss", 3),
        (8.0, 7.0, "• Undermined DEI initiatives\n• Reputation damage\n• Legal liability risk", 3),
        (8.0, 3.0, "• 2.5x higher absenteeism", 3),
        (3.0, 2.0, "• Diminished innovation", 3)
    ]
    
    for x, y, text, ring_idx in impacts:
        text_box = ax.text(x, y, text, fontsize=8, ha='center', va='center', 
                           bbox=dict(facecolor='white', alpha=0.9, 
                                     edgecolor=ripple_colors[ring_idx], 
                                     boxstyle='round,pad=0.3'))
    
    # Remove axes
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    fig.suptitle('Ripple Effects of Workplace Microaggressions', fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('microaggression_ripple_effects.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "microaggression_ripple_effects.png"

# Slide 6: Testimonial quotes visualization
def create_testimonial_quotes():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create speech bubbles with quotes
    quotes = [
        (0.25, 0.8, "Every time I speak in meetings, I feel\nlike I have to represent my entire race.\nIt's exhausting to constantly worry about\nreinforcing stereotypes.", accent_colors[0]),
        (0.75, 0.8, "I've stopped sharing my pronouns because\nI got tired of the eye rolls and\n'political correctness' comments.", accent_colors[1]),
        (0.25, 0.5, "After being told I'm 'surprisingly articulate'\nseveral times, I now obsess over every\nword I say in professional settings.", accent_colors[2]),
        (0.75, 0.5, "When colleagues constantly mispronounce\nmy name even after corrections, it feels\nlike they don't think I'm worth the effort.", accent_colors[3]),
        (0.25, 0.2, "I stopped sharing cultural perspectives\nafter being told 'we don't do things\nthat way here' one too many times.", accent_colors[4]),
        (0.75, 0.2, "Being complimented for being 'not like other\nwomen in leadership' made me question if\nI'm betraying my authentic self to fit in.", accent_colors[5])
    ]
    
    for x, y, text, color in quotes:
        # Create text with quote bubble
        text_box = ax.text(x, y, text, fontsize=10, ha='center', va='center',
                         bbox=dict(facecolor='white', alpha=0.9, edgecolor=color, 
                                   boxstyle='round,pad=0.6', linewidth=2))
    
    # Title and subtitle
    fig.suptitle('The Individual Impact of Workplace Microaggressions', 
                fontsize=16, fontweight='bold', y=0.98)
    ax.text(0.5, 0.05, "Research participant testimonials describing psychological and professional consequences", 
           fontsize=12, ha='center', style='italic')
    
    # Remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('microaggression_testimonials.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "microaggression_testimonials.png"

# Slide 7: Workplace scene with speech bubbles showing common microaggressions
def create_workplace_microaggression_scene():
    # This would be better with actual illustrations, but we'll create a simple diagram
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Create office layout background
    ax.add_patch(Rectangle((0, 0), 14, 8, facecolor='lightgray', alpha=0.3))
    
    # Meeting room
    ax.add_patch(Rectangle((1, 4), 4, 3, facecolor='lightblue', alpha=0.3, edgecolor='black'))
    ax.text(3, 6.8, "MEETING ROOM", fontsize=10, ha='center')
    
    # Break room
    ax.add_patch(Rectangle((9, 4), 4, 3, facecolor='lightgreen', alpha=0.3, edgecolor='black'))
    ax.text(11, 6.8, "BREAK ROOM", fontsize=10, ha='center')
    
    # Open work area
    ax.add_patch(Rectangle((4, 1), 6, 2, facecolor='lightyellow', alpha=0.3, edgecolor='black'))
    ax.text(7, 2.8, "OPEN WORK AREA", fontsize=10, ha='center')
    
    # Add stick figures (circles for heads)
    people = [
        # Meeting room people
        (2, 5, "Person A"),
        (2.5, 6, "Person B"),
        (3.5, 5.5, "Person C"),
        (4, 6, "Person D"),
        
        # Break room people
        (10, 5, "Person E"),
        (11, 6, "Person F"),
        (12, 5.5, "Person G"),
        
        # Open area people
        (5, 1.5, "Person H"),
        (7, 2, "Person I"),
        (8.5, 1.5, "Person J")
    ]
    
    # Draw people as circles
    for x, y, label in people:
        ax.add_patch(Circle((x, y), 0.2, facecolor='white', edgecolor='black'))
    
    # Add microaggression speech bubbles
    microaggressions = [
        (2.8, 5.2, "Wait, let me explain this\nagain in simpler terms...", accent_colors[0]), # Meeting
        (3.7, 6.3, "That's a great idea!\nDidn't John just say that?", accent_colors[1]), # Meeting
        
        (10.5, 5.3, "You're so well-spoken!\nWhere are you really from?", accent_colors[2]), # Break room
        (11.5, 6.4, "You don't look like\nan engineer!", accent_colors[3]), # Break room
        
        (5.5, 1.8, "I don't see disabilities.\nI treat everyone the same.", accent_colors[4]), # Open area
        (7.5, 2.3, "That's not what we meant.\nYou're being too sensitive.", accent_colors[5]), # Open area
    ]
    
    for x, y, text, color in microaggressions:
        text_box = ax.text(x, y, text, fontsize=8, ha='center', va='center',
                         bbox=dict(facecolor='white', alpha=0.9, edgecolor=color, 
                                   boxstyle='round,pad=0.3', linewidth=1.5))
    
    # Add structural microaggressions as notices on the wall
    structural = [
        (1, 0.5, "CULTURAL FIT:\nMust embrace our\nhappy-hour culture", accent_colors[6]),
        (7, 0.5, "PERFORMANCE REVIEW:\nMeasuring 'executive presence'\nand 'polish'", accent_colors[7]),
        (13, 0.5, "PROMOTION CRITERIA:\nMust be able to work\nunpredictable hours", accent_colors[0])
    ]
    
    for x, y, text, color in structural:
        text_box = ax.text(x, y, text, fontsize=8, ha='center', va='center',
                         bbox=dict(facecolor='lightyellow', alpha=0.9, edgecolor=color, 
                                   boxstyle='round,pad=0.3', linewidth=1.5))
    
    # Title
    fig.suptitle('Common Workplace Microaggressions', fontsize=16, fontweight='bold', y=0.98)
    
    # Remove axes
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('workplace_microaggressions.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "workplace_microaggressions.png"

# Slide 8: Reflection journal visualization
def create_reflection_journal():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create journal page background
    ax.add_patch(Rectangle((0, 0), 12, 8, facecolor='beige', alpha=0.3, edgecolor='brown', linewidth=2))
    
    # Add journal lines
    for y in np.arange(0.5, 8, 0.5):
        ax.axhline(y=y, color='brown', alpha=0.3, linestyle='-')
    
    # Add reflection entries with dates
    entries = [
        (0.2, 7.3, "February 3, 2025", "First class discussion on microaggressions - I realized I've experienced them but never\nhad language to describe what was happening. The concept of 'death by a thousand cuts' resonates.", accent_colors[0]),
        (0.2, 6.0, "February 17, 2025", "Uncomfortable realization today - I've definitely committed microinsults without intending to.\nI asked a colleague 'where are you really from?' last month without considering the implications.", accent_colors[1]),
        (0.2, 4.7, "March 2, 2025", "Case study analysis helped me see how intention doesn't equal impact. I need to focus less\non defending my intentions and more on understanding how my words affect others.", accent_colors[2]),
        (0.2, 3.4, "March 23, 2025", "Applied intervention strategies in group project when someone was repeatedly interrupted.\nUsed 'I'd like to hear X finish their point' technique. It worked well!", accent_colors[3]),
        (0.2, 2.1, "April 12, 2025", "Connected microaggressions to broader systems of inequity today. Now I see how these\n'small' moments reinforce larger patterns of exclusion in workplaces.", accent_colors[4]),
        (0.2, 0.8, "April 28, 2025", "Final reflection: This topic has transformed how I view workplace interactions.\nI now have tools to recognize, respond to, and prevent microaggressions in my future career.", accent_colors[5])
    ]
    
    for x, y, date, text, color in entries:
        # Date header
        ax.text(x, y, date, fontsize=10, fontweight='bold', color=color)
        
        # Entry text
        ax.text(x, y-0.3, text, fontsize=9)
    
    # Title
    fig.suptitle('Personal Reflection Journal: My Journey with Microaggressions', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Remove axes
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('reflection_journal.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "reflection_journal.png"

# Slide 9: Concept map connecting course materials
def create_concept_map():
    # Create a network graph
    G = nx.Graph()
    
    # Add central node
    G.add_node("Microaggressions", size=2000, color=colors[0])
    
    # Add main category nodes
    categories = ["Frameworks", "Theories", "Response\nStrategies", "Case\nStudies", "Personal\nExperiences"]
    for i, category in enumerate(categories):
        G.add_node(category, size=1000, color=colors[1])
        G.add_edge("Microaggressions", category, weight=2)
    
    # Add specific course materials
    materials = [
        ("Sue's\nCategorization", "Frameworks"),
        ("Nadal's Response\nGuide", "Response\nStrategies"),
        ("Essed's Everyday\nRacism", "Theories"),
        ("Cumulative\nImpact", "Theories"),
        ("Intersectionality", "Theories"),
        ("Healthcare\nSettings", "Case\nStudies"),
        ("Tech Industry", "Case\nStudies"),
        ("Education", "Case\nStudies"),
        ("Perspective\nTaking", "Personal\nExperiences"),
        ("Identity\nReflection", "Personal\nExperiences"),
        ("Ally\nInterventions", "Response\nStrategies"),
        ("Taxonomy of\nMicroaggressions", "Frameworks")
    ]
    
    for material, category in materials:
        G.add_node(material, size=500, color=colors[3])
        G.add_edge(category, material, weight=1)
    
    # Create positions for the network graph
    pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
    
    # Manually adjust positions for better layout
    pos["Microaggressions"] = np.array([0.5, 0.5])
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    radius = 0.3
    
    for i, category in enumerate(categories):
        pos[category] = np.array([0.5, 0.5]) + radius * np.array([np.cos(angles[i]), np.sin(angles[i])])
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Draw edges
    for u, v, data in G.edges(data=True):
        weight = data['weight']
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], 
                linewidth=weight, color='gray', alpha=0.7)
    
    # Draw nodes
    for node in G.nodes():
        size = G.nodes[node].get('size', 300)
        color = G.nodes[node].get('color', 'blue')
        
        circle = plt.Circle(pos[node], 
                         radius=np.sqrt(size)/100, 
                         color=color, 
                         alpha=0.7,
                         edgecolor='black')
        ax.add_patch(circle)
        
        # Add text with white background for readability
        text = ax.text(pos[node][0], pos[node][1], node, 
                     ha='center', va='center', fontsize=9, fontweight='bold')
        text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    # Set title
    fig.suptitle('Concept Map: Course Materials on Microaggressions', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('concept_map.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "concept_map.png"

# Slide 10: Decision tree for identifying microaggressions
def create_decision_tree():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Main nodes
    nodes = [
        # Level 1
        (0.5, 0.9, "Is this comment, behavior, or practice potentially problematic?", colors[0]),
        
        # Level 2
        (0.3, 0.75, "Does it relate to an\naspect of marginalized identity?", colors[1]),
        (0.7, 0.75, "Does it make assumptions\nabout an individual or group?", colors[1]),
        
        # Level 3
        (0.15, 0.6, "Could it reinforce\nstereotypes?", colors[2]),
        (0.4, 0.6, "Does it dismiss or\ninvalidate experiences?", colors[2]),
        (0.6, 0.6, "Does it overemphasize or\nexoticize differences?", colors[2]),
        (0.85, 0.6, "Does it impose dominant\ngroup norms?", colors[2]),
        
        # Level 4 - Examples
        (0.15, 0.4, "Example: \"You're so articulate\"\n(implies surprise based on identity)", colors[3]),
        (0.4, 0.4, "Example: \"I don't see color\"\n(invalidates racial experiences)", colors[3]),
        (0.6, 0.4, "Example: \"Your hair is so interesting.\nCan I touch it?\"", colors[3]),
        (0.85, 0.4, "Example: \"That food smells strange.\nCould you eat it elsewhere?\"", colors[3]),
        
        # Level 5 - Recognition
        (0.15, 0.25, "LIKELY MICROINSULT", accent_colors[1]),
        (0.4, 0.25, "LIKELY MICROINVALIDATION", accent_colors[2]),
        (0.6, 0.25, "LIKELY MICROINSULT", accent_colors[1]),
        (0.85, 0.25, "LIKELY MICROASSAULT", accent_colors[0]),
        
        # Level 6 - Response suggestions
        (0.15, 0.15, "Response: \"What do you mean by 'articulate'?\nWhat were you expecting?\"", accent_colors[5]),
        (0.4, 0.15, "Response: \"While that's well-intentioned,\nnot 'seeing' race can erase important experiences\"", accent_colors[5]),
        (0.6, 0.15, "Response: \"Please don't comment on or touch\npeople's physical features\"", accent_colors[5]),
        (0.85, 0.15, "Response: \"Food preferences vary.\nLet's ensure all cultural foods are welcome\"", accent_colors[5])
    ]
    
    # Draw nodes
    for x, y, text, color in nodes:
        circle = plt.Circle((x, y), 0.03, color=color, zorder=5)
        ax.add_patch(circle)
        
        # Add text with background for readability
        text_box = ax.text(x, y-0.05, text, ha='center', va='top', fontsize=8,
                         bbox=dict(facecolor='white', alpha=0.7, edgecolor=color, boxstyle='round,pad=0.3'))
    
    # Connect nodes with arrows
    connections = [
        # Level 1 to 2
        (0.5, 0.9, 0.3, 0.75),
        (0.5, 0.9, 0.7, 0.75),
        
        # Level 2 to 3
        (0.3, 0.75, 0.15, 0.6),
        (0.3, 0.75, 0.4, 0.6),
        (0.7, 0.75, 0.6, 0.6),
        (0.7, 0.75, 0.85, 0.6),
        
        # Level 3 to 4
        (0.15, 0.6, 0.15, 0.4),
        (0.4, 0.6, 0.4, 0.4),
        (0.6, 0.6, 0.6, 0.4),
        (0.85, 0.6, 0.85, 0.4),
        
        # Level 4 to 5
        (0.15, 0.4, 0.15, 0.25),
        (0.4, 0.4, 0.4, 0.25),
       (0.6, 0.4, 0.6, 0.25),
       (0.85, 0.4, 0.85, 0.25),
       
       # Level 5 to 6
       (0.15, 0.25, 0.15, 0.15),
       (0.4, 0.25, 0.4, 0.15),
       (0.6, 0.25, 0.6, 0.15),
       (0.85, 0.25, 0.85, 0.15)
   ]
   
   # Draw connections
for x1, y1, x2, y2 in connections:
       ax.annotate("", 
                  xy=(x2, y2), xycoords='data',
                  xytext=(x1, y1), textcoords='data',
                  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.1",
                                  color='gray', alpha=0.7, linewidth=1))
   
   # Title
fig.suptitle('Decision Tree for Identifying Potential Microaggressions', 
               fontsize=16, fontweight='bold', y=0.98)
   
   # Note at bottom
   ax.text(0.5, 0.05, "Note: This simplified decision tree is a starting point for recognition.\nAlways consider context, power dynamics, and individual experiences.", 
          ha='center', fontsize=9, style='italic')
   
   # Remove axes
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis('off')
   
   plt.tight_layout()
   plt.savefig('decision_tree.png', dpi=300, bbox_inches='tight')
   plt.close()
   
   return "decision_tree.png"

# Slide 11: Role-play scenarios with response strategies
def create_response_strategies():
   fig, ax = plt.subplots(figsize=(12, 8))
   
   # Create three scenario boxes
   scenarios = [
       (0.2, 0.7, "WHEN WITNESSING\nMICROAGGRESSIONS", accent_colors[0]),
       (0.5, 0.7, "WHEN COMMITTING\nMICROAGGRESSIONS", accent_colors[1]),
       (0.8, 0.7, "WHEN EXPERIENCING\nMICROAGGRESSIONS", accent_colors[2])
   ]
   
   for x, y, title, color in scenarios:
       # Create scenario box
       rect = Rectangle((x-0.15, y-0.25), 0.3, 0.3, facecolor=color, alpha=0.2, 
                         edgecolor=color, linewidth=2)
       ax.add_patch(rect)
       ax.text(x, y, title, ha='center', va='center', fontsize=10, fontweight='bold')
   
   # Add speech bubbles with example language
   examples = [
       # Witnessing
       (0.2, 0.5, "QUESTION:\n\"Can you explain what you meant by that comment?\"", accent_colors[0]),
       (0.2, 0.35, "PAUSE:\n\"Let's take a moment to consider the impact of that statement.\"", accent_colors[0]),
       (0.2, 0.2, "EDUCATE:\n\"I've learned that comments like that can reinforce stereotypes\nbecause...\"", accent_colors[0]),
       
       # Committing
       (0.5, 0.5, "LISTEN:\n\"Thank you for pointing that out. I want to understand better.\"", accent_colors[1]),
       (0.5, 0.35, "ACKNOWLEDGE:\n\"I see how my comment had an impact I didn't intend.\nI apologize.\"", accent_colors[1]),
       (0.5, 0.2, "CHANGE:\n\"I'm going to be more mindful about this. Could you suggest\na better way I could have expressed that?\"", accent_colors[1]),
       
       # Experiencing
       (0.8, 0.5, "ASSESS:\n\"Is this a safe moment to respond? What's my goal here?\"", accent_colors[2]),
       (0.8, 0.35, "RESPOND:\n\"When you [specific action], it [specific impact]. \nInstead, could you [alternative]?\"", accent_colors[2]),
       (0.8, 0.2, "SUPPORT:\n\"I'd like to discuss this with [ally/supervisor/HR]\nto address the pattern.\"", accent_colors[2])
   ]
   
   for x, y, text, color in examples:
       text_box = ax.text(x, y, text, fontsize=9, ha='center', va='center',
                        bbox=dict(facecolor='white', alpha=0.9, edgecolor=color, 
                                  boxstyle='round,pad=0.4', linewidth=1.5))
   
   # Title
   fig.suptitle('Response Strategies for Workplace Microaggressions', 
               fontsize=16, fontweight='bold', y=0.98)
   
   # Remove axes
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis('off')
   
   plt.tight_layout()
   plt.savefig('response_strategies.png', dpi=300, bbox_inches='tight')
   plt.close()
   
   return "response_strategies.png"

# Slide 12: Implementation roadmap for organizations
def create_implementation_roadmap():
   fig, ax = plt.subplots(figsize=(14, 8))
   
   # Create a roadmap with 3 stages
   stages = ["AWARENESS STAGE", "IMPLEMENTATION STAGE", "INTEGRATION STAGE"]
   stage_positions = [0.2, 0.5, 0.8]
   stage_colors = [accent_colors[0], accent_colors[1], accent_colors[2]]
   
   # Draw the main path
   ax.plot([0.1, 0.9], [0.5, 0.5], 'k-', linewidth=3, alpha=0.3)
   
   # Add stage markers and labels
   for i, (pos, stage, color) in enumerate(zip(stage_positions, stages, stage_colors)):
       # Stage marker
       circle = plt.Circle((pos, 0.5), 0.05, facecolor=color, edgecolor='black', zorder=5)
       ax.add_patch(circle)
       
       # Stage label
       ax.text(pos, 0.6, stage, ha='center', va='center', fontsize=12, fontweight='bold')
       
       # Stage number
       ax.text(pos, 0.5, str(i+1), ha='center', va='center', fontsize=10, fontweight='bold', color='white')
   
   # Add action items for each stage
   actions = [
       # Awareness Stage
       (0.2, 0.8, "LEADERSHIP", "• Education on microaggression impact\n• Commitment to addressing patterns\n• Modeling appropriate responses", accent_colors[0]),
       (0.2, 0.3, "TEAM LEVEL", "• Awareness training for all employees\n• Creating common vocabulary\n• Establishing baseline metrics", accent_colors[0]),
       
       # Implementation Stage
       (0.5, 0.8, "LEADERSHIP", "• Develop formal response protocols\n• Train managers as first responders\n• Create accountability systems", accent_colors[1]),
       (0.5, 0.3, "TEAM LEVEL", "• Practice intervention strategies\n• Implement feedback mechanisms\n• Develop team-specific guidelines", accent_colors[1]),
       
       # Integration Stage
       (0.8, 0.8, "LEADERSHIP", "• Integrate into performance evaluations\n• Regular climate assessment\n• Continuous improvement processes", accent_colors[2]),
       (0.8, 0.3, "TEAM LEVEL", "• Peer coaching and mentoring\n• Regular reflection practices\n• Community of practice development", accent_colors[2])
   ]
   
   for x, y, title, text, color in actions:
       # Create action box
       rect = Rectangle((x-0.15, y-0.15), 0.3, 0.3, facecolor=color, alpha=0.1, 
                      edgecolor=color, linewidth=1.5)
       ax.add_patch(rect)
       
       # Add title and text
       ax.text(x, y+0.1, title, ha='center', va='center', fontsize=9, fontweight='bold')
       ax.text(x, y-0.02, text, ha='center', va='center', fontsize=8)
   
   # Connect action items to stages with dotted lines
   for x, y, _, _, _ in actions:
       ax.plot([x, x], [0.5, y-0.15 if y < 0.5 else y+0.15], 'k:', linewidth=1, alpha=0.5)
   
   # Title
   fig.suptitle('Organizational Implementation Roadmap for Addressing Microaggressions', 
               fontsize=16, fontweight='bold', y=0.98)
   
   # Timeline at bottom
   timeline_months = ["Month 1-2", "Month 3-6", "Month 7+"]
   for i, (pos, months) in enumerate(zip(stage_positions, timeline_months)):
       ax.text(pos, 0.1, months, ha='center', va='center', fontsize=9, style='italic')
   
   # Remove axes
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis('off')
   
   plt.tight_layout()
   plt.savefig('implementation_roadmap.png', dpi=300, bbox_inches='tight')
   plt.close()
   
   return "implementation_roadmap.png"

# Slide 13: Personal development plan
def create_personal_development_plan():
   fig, ax = plt.subplots(figsize=(12, 8))
   
   # Create clipboard background
   ax.add_patch(Rectangle((0.05, 0.05), 0.9, 0.85, facecolor='bisque', edgecolor='brown', linewidth=2))
   ax.add_patch(Rectangle((0.4, 0.9), 0.2, 0.05, facecolor='silver', edgecolor='gray', linewidth=1))
   
   # Add title
   ax.text(0.5, 0.85, "PERSONAL DEVELOPMENT PLAN", fontsize=14, fontweight='bold', ha='center')
   ax.text(0.5, 0.81, "Microaggression Awareness and Response Development", fontsize=10, style='italic', ha='center')
   
   # Add today's date
   today = datetime.datetime.now().strftime("%B %d, %Y")
   ax.text(0.1, 0.77, f"Date: {today}", fontsize=9)
   
   # Create three focus areas
   focus_areas = [
       (0.2, 0.7, "KNOWLEDGE DEVELOPMENT", accent_colors[0]),
       (0.5, 0.7, "SKILL BUILDING", accent_colors[1]),
       (0.8, 0.7, "APPLICATION & MEASUREMENT", accent_colors[2])
   ]
   
   for x, y, title, color in focus_areas:
       # Create focus area box
       rect = Rectangle((x-0.15, y-0.025), 0.3, 0.05, facecolor=color, alpha=0.3, 
                      edgecolor=color, linewidth=1.5)
       ax.add_patch(rect)
       ax.text(x, y, title, ha='center', va='center', fontsize=10, fontweight='bold')
   
   # Add goals and timelines
   goals = [
       # Knowledge Development
       (0.2, 0.65, "Goal 1: Read two additional books on microaggression research", "Jul 2025", accent_colors[0]),
       (0.2, 0.55, "Goal 2: Subscribe to DEI research journal for ongoing updates", "Jun 2025", accent_colors[0]),
       (0.2, 0.45, "Goal 3: Join online community focused on inclusive practices", "Aug 2025", accent_colors[0]),
       
       # Skill Building
       (0.5, 0.65, "Goal 1: Practice 'Question, Pause, Educate' intervention in 3 scenarios", "Jun-Jul 2025", accent_colors[1]),
       (0.5, 0.55, "Goal 2: Develop personal script library for common situations", "Jul 2025", accent_colors[1]),
       (0.5, 0.45, "Goal 3: Attend advanced workshop on facilitating difficult conversations", "Sep 2025", accent_colors[1]),
       
       # Application & Measurement
       (0.8, 0.65, "Goal 1: Keep reflection journal documenting interventions and outcomes", "Ongoing", accent_colors[2]),
       (0.8, 0.55, "Goal 2: Request feedback from 3 colleagues on communication patterns", "Aug 2025", accent_colors[2]),
       (0.8, 0.45, "Goal 3: Conduct personal climate assessment in team environment", "Oct 2025", accent_colors[2])
   ]
   
   for x, y, text, timeline, color in goals:
       ax.text(x-0.15, y, text, fontsize=8, va='center')
       ax.text(x+0.12, y, timeline, fontsize=8, va='center', style='italic', color=color)
   
   # Add progress tracking section
   ax.add_patch(Rectangle((0.1, 0.15), 0.8, 0.2, facecolor='white', edgecolor='brown', linewidth=1))
   ax.text(0.5, 0.32, "PROGRESS TRACKING", ha='center', fontsize=10, fontweight='bold')
   
   # Add tracking rows
   tracking = [
       ("Goal completion rate:", "0/9 (0%)", "3/9 (33%)", "6/9 (67%)", "9/9 (100%)"),
       ("Self-assessment rating:", "Awareness", "Development", "Competence", "Mastery"),
       ("Intervention confidence:", "Low", "Moderate", "High", "Expert")
   ]
   
   headers = ["Metric", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026"]
   col_positions = [0.15, 0.3, 0.45, 0.6, 0.75]
   
   for i, header in enumerate(headers):
       ax.text(col_positions[i], 0.28, header, fontsize=8, fontweight='bold', ha='center')
   
   for i, row in enumerate(tracking):
       y_pos = 0.24 - i*0.03
       for j, cell in enumerate(row):
           ax.text(col_positions[j], y_pos, cell, fontsize=7, ha='center')
   
   # Add signature line
   ax.axhline(y=0.1, xmin=0.1, xmax=0.4, color='black', linewidth=1)
   ax.text(0.25, 0.08, "Personal Signature", fontsize=8, ha='center')
   
   # Add review date
   ax.text(0.7, 0.1, "Next Review Date: October 15, 2025", fontsize=8, ha='center')
   
   # Remove axes
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis('off')
   
   plt.tight_layout()
   plt.savefig('personal_development_plan.png', dpi=300, bbox_inches='tight')
   plt.close()
   
   return "personal_development_plan.png"

# Slide 14: Circular diagram showing continuous improvement cycle
def create_continuous_improvement():
   fig, ax = plt.subplots(figsize=(10, 10))
   
   # Define the continuous improvement cycle stages
   stages = ["RECOGNIZE", "RESPOND", "REFLECT", "REVISE"]
   angles = np.linspace(0, 2*np.pi, len(stages), endpoint=False)
   angles = angles + np.pi/4  # Rotate to position first item at top
   
   # Create the main circle
   circle = plt.Circle((0.5, 0.5), 0.3, facecolor='none', edgecolor='black', linewidth=2, alpha=0.7)
   ax.add_patch(circle)
   
   # Add stage labels along the circle
   for i, (stage, angle) in enumerate(zip(stages, angles)):
       x = 0.5 + 0.3 * np.cos(angle)
       y = 0.5 + 0.3 * np.sin(angle)
       
       # Create node
       node_circle = plt.Circle((x, y), 0.08, facecolor=accent_colors[i], edgecolor='black', alpha=0.8)
       ax.add_patch(node_circle)
       
       # Add label
       ax.text(x, y, stage, ha='center', va='center', fontsize=10, fontweight='bold')
       
       # Add arrow to next stage
       next_angle = angles[(i + 1) % len(stages)]
       next_x = 0.5 + 0.3 * np.cos(next_angle)
       next_y = 0.5 + 0.3 * np.sin(next_angle)
       
       # Calculate intermediate points for curved arrow
       mid_angle = (angle + next_angle) / 2
       ctrl_x = 0.5 + 0.4 * np.cos(mid_angle)
       ctrl_y = 0.5 + 0.4 * np.sin(mid_angle)
       
       # Draw curved arrow using a path
       arrow_path = plt.matplotlib.path.Path(
           [(x, y), (ctrl_x, ctrl_y), (next_x, next_y)],
           [plt.matplotlib.path.Path.MOVETO, plt.matplotlib.path.Path.CURVE3, plt.matplotlib.path.Path.CURVE3]
       )
       arrow_patch = plt.matplotlib.patches.PathPatch(
           arrow_path, facecolor='none', edgecolor='black', linewidth=1.5,
           arrowstyle='->', connectionstyle='arc3,rad=0.3'
       )
       ax.add_patch(arrow_patch)
   
   # Add descriptions for each stage
   descriptions = [
       # RECOGNIZE
       (0.5, 0.9, "• Identify potential microaggressions\n• Notice patterns in environments\n• Understand impact on individuals\n• Recognize own biases and behaviors", accent_colors[0]),
       
       # RESPOND
       (0.9, 0.5, "• Apply appropriate intervention strategies\n• Consider context and safety\n• Practice allyship when witnessing\n• Use non-defensive communication", accent_colors[1]),
       
       # REFLECT
       (0.5, 0.1, "• Analyze effectiveness of responses\n• Seek feedback from affected parties\n• Document patterns and outcomes\n• Connect to broader systems", accent_colors[2]),
       
       # REVISE
       (0.1, 0.5, "• Adjust strategies based on feedback\n• Develop new communication skills\n• Implement structural changes\n• Share learning with others", accent_colors[3])
   ]
   
   for x, y, text, color in descriptions:
       text_box = ax.text(x, y, text, fontsize=9, ha='center', va='center',
                        bbox=dict(facecolor='white', alpha=0.9, edgecolor=color, 
                                  boxstyle='round,pad=0.3'))
   
   # Add central concept
   ax.text(0.5, 0.5, "CONTINUOUS\nIMPROVEMENT", fontsize=12, fontweight='bold', ha='center', va='center')
   
   # Title
   fig.suptitle('Continuous Improvement Cycle for Microaggression Awareness', 
               fontsize=16, fontweight='bold', y=0.98)
   
   # Remove axes
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis('off')
   
   plt.tight_layout()
   plt.savefig('continuous_improvement.png', dpi=300, bbox_inches='tight')
   plt.close()
   
   return "continuous_improvement.png"

# Create all visuals and return a list of filenames
def create_all_visuals():
   visuals = [
       create_iceberg_diagram(),                # Slide 2
       create_microaggression_types_chart(),    # Slide 3
       create_research_timeline(),              # Slide 4
       create_ripple_effect_infographic(),      # Slide 5
       create_testimonial_quotes(),             # Slide 6
       create_workplace_microaggression_scene(),# Slide 7
       create_reflection_journal(),             # Slide 8
       create_concept_map(),                    # Slide 9
       create_decision_tree(),                  # Slide 10
       create_response_strategies(),            # Slide 11
       create_implementation_roadmap(),         # Slide 12
       create_personal_development_plan(),      # Slide 13
       create_continuous_improvement()          # Slide 14
   ]
   
   return visuals

# Run the function to create all visuals
visual_files = create_all_visuals()
print("Created the following visual files:")
for i, file in enumerate(visual_files):
   print(f"Slide {i+2}: {file}")
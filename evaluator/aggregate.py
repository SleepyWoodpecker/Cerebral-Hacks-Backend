import collections as clt


def average_rating(user_output: list[dict]):
    total = 0.0
    for user in user_output:
        print(user)
        total += user["rating"]
    return total / len(user_output)


def action_breakdown(user_output: list[dict]):
    actions = [user["action"] for user in user_output]
    counts = clt.Counter(actions)
    return {
        "purchase": counts["purchase"],
        "like": counts["like"],
        "view": counts["view"],
        "total": len(user_output),
    }


if __name__ == "__main__":
    data = [
        {
            "id": 1,
            "rating": 4,
            "explanation": "Takeshi, the tech-savvy young professional, would likely appreciate the durable die-cast construction and the overall design of the Hot Wheels Monster Jam Titan Truck. The large monster truck wheels and the aggressive, sporty styling would appeal to his active lifestyle and interest in the latest gadgets and electronics.",
            "improvement": "To make the product more attractive to Takeshi, the manufacturer could consider adding some additional customization or personalization options, such as the ability to change the color scheme or include LED lights or other electronic features that would enhance the playing experience.",
            "action": "purchase",
        },
        {
            "id": 2,
            "rating": 3,
            "explanation": "Sakura, the lively university student, may find the Hot Wheels Monster Jam Titan Truck to be a bit too rugged and masculine for her personal style. While she appreciates unique and quirky items, the overall design of the truck may not align with her vibrant and youthful fashion sense.",
            "improvement": "To make the product more appealing to Sakura, the manufacturer could consider offering a version with a more colorful and customizable design, perhaps incorporating elements of traditional Japanese style or incorporating glitter and other decorative touches that would better match her personal aesthetic.",
            "action": "view",
        },
        {
            "id": 3,
            "rating": 4,
            "explanation": "Hiro, the busy father of two, would likely find the Hot Wheels Monster Jam Titan Truck to be a great option for his family. The durable construction and large, rugged wheels would make it suitable for outdoor play and exploration, and the classic Monster Jam branding would appeal to his children. Hiro values practicality and comfort, so the truck's design would fit well with his lifestyle.",
            "improvement": "To make the product even more appealing to Hiro, the manufacturer could consider offering a version with additional accessories or play features that would encourage family-friendly activities, such as the ability to connect multiple trucks for head-to-head races or the inclusion of a carrying case for easy transportation.",
            "action": "purchase",
        },
        {
            "id": 4,
            "rating": 5,
            "explanation": "Emi, the young and sporty individual living in Sapporo, would be highly interested in the Hot Wheels Monster Jam Titan Truck. As an avid outdoor enthusiast, she would appreciate the truck's durable construction and high-performance features, which would be well-suited for her active lifestyle and the snowy terrain of her hometown.",
            "improvement": "Given Emi's strong interest in the product, no major improvements are necessary. The manufacturer could potentially consider offering a version with specialized equipment or accessories designed for use in colder climates, such as snow chains or a specialized carrying case.",
            "action": "purchase",
        },
        {
            "id": 5,
            "rating": 4,
            "explanation": "Takumi, the young tech-savvy professional in Kobe, would likely find the Hot Wheels Monster Jam Titan Truck to be an appealing purchase. The durable construction and eye-catching design would align with his minimalistic, modern style, and the high-performance features would cater to his interest in the latest technology and innovations.",
            "improvement": "To further enhance the product's appeal to Takumi, the manufacturer could consider incorporating some additional smart or interactive features, such as the ability to connect the truck to a mobile app for customization or control, or the inclusion of LED lights or other electronic components that would add a touch of technological sophistication.",
            "action": "purchase",
        },
        {
            "id": 6,
            "rating": 3,
            "explanation": "Aya, the university student with diverse interests, may have a mixed reaction to the Hot Wheels Monster Jam Titan Truck. While she appreciates a range of styles, the truck's masculine and sporty design may not fully align with her eclectic wardrobe and preference for more versatile and adaptable products.",
            "improvement": "To make the product more appealing to Aya, the manufacturer could consider offering a version with a more customizable or gender-neutral design, allowing her to personalize the truck to better fit her personal style and preferences. This could include the ability to swap out certain elements or choose from a wider range of color options.",
            "action": "view",
        },
        {
            "id": 7,
            "rating": 4,
            "explanation": "Takeo, the middle-aged professional in Nagoya, would likely find the Hot Wheels Monster Jam Titan Truck to be a suitable purchase. As a busy executive with a sporty side, he would appreciate the truck's durable construction and high-performance features, which would complement his active lifestyle and practical wardrobe.",
            "improvement": "To further enhance the product's appeal to Takeo, the manufacturer could consider offering a version with more premium or sophisticated design elements, such as a sleeker body shape or the use of higher-quality materials, to better match his refined personal style and status as a successful professional.",
            "action": "purchase",
        },
        {
            "id": 8,
            "rating": 4,
            "explanation": "Ami, the young, tech-savvy professional in Hiroshima, would likely be drawn to the Hot Wheels Monster Jam Titan Truck. With her keen eye for design and love for the latest gadgets, she would appreciate the truck's durable construction and rugged, modern styling, which would complement her minimalistic and practical wardrobe.",
            "improvement": "To further enhance the product's appeal to Ami, the manufacturer could consider incorporating some additional technological features or customization options, such as the ability to connect the truck to a mobile app for advanced control or the inclusion of LED lights or other electronic components that would add a touch of high-tech sophistication.",
            "action": "purchase",
        },
        {
            "id": 9,
            "rating": 5,
            "explanation": "Ryuichi, the sporty and health-conscious individual in Yokohama, would be highly interested in the Hot Wheels Monster Jam Titan Truck. As an avid outdoor enthusiast, he would appreciate the truck's durable construction, large monster truck wheels, and overall design, which would be well-suited for his active lifestyle and the varied terrain of his coastal hometown.",
            "improvement": "Given Ryuichi's strong interest in the product, no major improvements are necessary. The manufacturer could potentially consider offering a version with specialized accessories or features tailored to the needs of outdoor enthusiasts, such as enhanced shock absorption or the ability to withstand more rugged environments.",
            "action": "purchase",
        },
        {
            "id": 10,
            "rating": 4,
            "explanation": "Akiko, the young, ambitious university student in Kobe, would likely find the Hot Wheels Monster Jam Titan Truck to be an appealing purchase. With her strong passion for technology and innovation, she would appreciate the truck's modern design and durable construction, which would complement her minimalistic style and interest in the latest gadgets.",
            "improvement": "To further enhance the product's appeal to Akiko, the manufacturer could consider incorporating some additional technological features or customization options, such as the ability to connect the truck to a mobile app for advanced control or the inclusion of programmable LED lights or other electronic components that would add a touch of high-tech sophistication.",
            "action": "purchase",
        },
    ]
    print(average_rating(data))
    print(action_breakdown(data))

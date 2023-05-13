from website.models import Product
import csv
import chardet


def run():
    with open('scripts/petsplace_data_apotheek.csv', 'rb') as file:
        # detect the encoding of the file
        result = chardet.detect(file.read())
        encoding = result['encoding']

    with open('scripts/petsplace_data_apotheek.csv', 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)

        # Product.objects.all().delete()
        c = 0
        for row in reader:
            print(c)
            c += 1
            # print(row)
            # try:
            #     unit_amount2 = '%g' % (float(row[5].replace(',', '.')))
            # except ValueError:
            #     try:
            #         unit_amount2 = '%g' % (float(int(eval(row[5]))))
            #     except:
            #         continue
            # except NameError:
            #     unit_amount2 = float("1")
            # print(row[4]+str(unit_amount2)+row[6])
            name1 = [x.strip() for x in row[4].split('-')]
            name2 = "".join(name1).replace(
                "/", "_").replace("&", "and").replace(" ", "_").replace("<", "").replace(">", "")
            print(name2)
            product = Product(store=row[0],
                              animal=row[1],
                              category=row[2],
                              brand=row[3],
                              product_title=row[4],
                              normal_price=float(row[5].replace(',', '.')),
                              sale_price=float(row[6].replace(',', '.')),
                              sale=row[7],
                              age_group=row[8],
                              product_page_url=row[9],
                              image="products/"+name2+".jpg")
            product.save()

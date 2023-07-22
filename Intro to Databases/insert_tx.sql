set schema 'shopify';

begin transaction;

insert into apps (id, url, title, developer, developer_link, icon, reviews_count) 
values ('example_id', 'https://apps.shopify.com/example','example', 'JordanGrahamRepo', 'https://apps.shopify.com/partners/example',         'https://apps.shopifycdn.com/listing_images/example/icon/example.png?height=72&width=72',
2);

insert into reviews (app_id, author, rating, posted_at)
values ('example_id', 'Jordan', '5', '2022-02-23');

insert into reviews (app_id, author, rating, posted_at)
values ('example_id', 'Graham', '4', '2022-02-23');

commit;
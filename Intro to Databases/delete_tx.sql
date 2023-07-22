set schema 'shopify';

begin transaction;

delete from reviews where app_id = 'example_id';

delete from apps where id = 'example_id';

commit;


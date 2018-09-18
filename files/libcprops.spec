Name: libcprops
Version: 0.1.12
Release:  0
Summary: the c prototyping tools library provides thread-safe linked list, priority queue, hash table, hash list, AVL tree and trie implementations, as well as a thread pool and thread management framework, a tcp and http socket api, and a dbms abstraction layer.
Group: http://cprops.sourceforge.net/
License: GPL
URL: http://cprops.sourceforge.net/
Vendor: http://cprops.sourceforge.net/
Source: https://sourceforge.net/projects/cprops/files/cprops/cprops-0.1.12/libcprops-0.1.12.zip
Prefix: %{_prefix}
Packager: Christopher J. Olido
BuildRoot: %{_tmppath}/%{name}-root

%description
the c prototyping tools library provides thread-safe linked list, priority queue, hash table, hash list, AVL tree and trie implementations, as well as a thread pool and thread management framework, a tcp and http socket api, and a dbms abstraction layer.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

/usr/bin/Makefile.cpsp
/usr/bin/cpsp
/usr/bin/cpsp-gen.sh
/usr/bin/cpsvc
/usr/bin/mime.types
/usr/include/cprops/avl.h
/usr/include/cprops/bstr.h
/usr/include/cprops/client.h
/usr/include/cprops/collection.h
/usr/include/cprops/common.h
/usr/include/cprops/config.h
/usr/include/cprops/db.h
/usr/include/cprops/hashlist.h
/usr/include/cprops/hashtable.h
/usr/include/cprops/heap.h
/usr/include/cprops/http.h
/usr/include/cprops/httpclient.h
/usr/include/cprops/linked_list.h
/usr/include/cprops/log.h
/usr/include/cprops/mempool.h
/usr/include/cprops/mtab.h
/usr/include/cprops/multimap.h
/usr/include/cprops/nary.h
/usr/include/cprops/priority_list.h
/usr/include/cprops/rb.h
/usr/include/cprops/rtrie.h
/usr/include/cprops/socket.h
/usr/include/cprops/sorted_hash.h
/usr/include/cprops/splay.h
/usr/include/cprops/str.h
/usr/include/cprops/thread.h
/usr/include/cprops/trie.h
/usr/include/cprops/util.h
/usr/include/cprops/vector.h
/usr/include/cprops/wtab.h
/usr/include/cprops/wtrie.h
/usr/lib/libcprops.a
/usr/lib/libcprops.la
/usr/lib/libcprops.so
/usr/lib/libcprops.so.15
/usr/lib/libcprops.so.15.0.0
/usr/share/man/man3/cp_avltree.3.gz
/usr/share/man/man3/cp_avltree_callback.3.gz
/usr/share/man/man3/cp_avltree_contains.3.gz
/usr/share/man/man3/cp_avltree_count.3.gz
/usr/share/man/man3/cp_avltree_create.3.gz
/usr/share/man/man3/cp_avltree_create_by_option.3.gz
/usr/share/man/man3/cp_avltree_delete.3.gz
/usr/share/man/man3/cp_avltree_destroy.3.gz
/usr/share/man/man3/cp_avltree_destroy_custom.3.gz
/usr/share/man/man3/cp_avltree_get.3.gz
/usr/share/man/man3/cp_avltree_get_mode.3.gz
/usr/share/man/man3/cp_avltree_insert.3.gz
/usr/share/man/man3/cp_avltree_lock.3.gz
/usr/share/man/man3/cp_avltree_rdlock.3.gz
/usr/share/man/man3/cp_avltree_set_mode.3.gz
/usr/share/man/man3/cp_avltree_unlock.3.gz
/usr/share/man/man3/cp_avltree_unset_mode.3.gz
/usr/share/man/man3/cp_avltree_wrlock.3.gz
/usr/share/man/man3/cp_bstr.3.gz
/usr/share/man/man3/cp_bstr_cat.3.gz
/usr/share/man/man3/cp_bstr_cmp.3.gz
/usr/share/man/man3/cp_bstr_cpy.3.gz
/usr/share/man/man3/cp_bstr_create.3.gz
/usr/share/man/man3/cp_bstr_destroy.3.gz
/usr/share/man/man3/cp_bstr_dump.3.gz
/usr/share/man/man3/cp_bstr_dup.3.gz
/usr/share/man/man3/cp_bstr_shift_left.3.gz
/usr/share/man/man3/cp_bstr_to_string.3.gz
/usr/share/man/man3/cp_client.3.gz
/usr/share/man/man3/cp_client_close.3.gz
/usr/share/man/man3/cp_client_connect.3.gz
/usr/share/man/man3/cp_client_create.3.gz
/usr/share/man/man3/cp_client_create_ssl.3.gz
/usr/share/man/man3/cp_client_destroy.3.gz
/usr/share/man/man3/cp_client_get_server_certificate.3.gz
/usr/share/man/man3/cp_client_read.3.gz
/usr/share/man/man3/cp_client_read_string.3.gz
/usr/share/man/man3/cp_client_set_retry.3.gz
/usr/share/man/man3/cp_client_ssl_init.3.gz
/usr/share/man/man3/cp_client_ssl_shutdown.3.gz
/usr/share/man/man3/cp_client_verify_hostname.3.gz
/usr/share/man/man3/cp_client_write.3.gz
/usr/share/man/man3/cp_client_write_string.3.gz
/usr/share/man/man3/cp_connection_descriptor.3.gz
/usr/share/man/man3/cp_data_source_destroy.3.gz
/usr/share/man/man3/cp_data_source_get_connection.3.gz
/usr/share/man/man3/cp_db_connection_close.3.gz
/usr/share/man/man3/cp_db_connection_close_statement.3.gz
/usr/share/man/man3/cp_db_connection_commit.3.gz
/usr/share/man/man3/cp_db_connection_destroy.3.gz
/usr/share/man/man3/cp_db_connection_escape_binary.3.gz
/usr/share/man/man3/cp_db_connection_escape_string.3.gz
/usr/share/man/man3/cp_db_connection_execute_statement.3.gz
/usr/share/man/man3/cp_db_connection_execute_statement_args.3.gz
/usr/share/man/man3/cp_db_connection_pool_create.3.gz
/usr/share/man/man3/cp_db_connection_pool_destroy.3.gz
/usr/share/man/man3/cp_db_connection_pool_get_connection.3.gz
/usr/share/man/man3/cp_db_connection_pool_release_connection.3.gz
/usr/share/man/man3/cp_db_connection_pool_set_blocking.3.gz
/usr/share/man/man3/cp_db_connection_pool_shutdown.3.gz
/usr/share/man/man3/cp_db_connection_prepare_statement.3.gz
/usr/share/man/man3/cp_db_connection_rollback.3.gz
/usr/share/man/man3/cp_db_connection_select.3.gz
/usr/share/man/man3/cp_db_connection_set_autocommit.3.gz
/usr/share/man/man3/cp_db_connection_set_fetch_metadata.3.gz
/usr/share/man/man3/cp_db_connection_set_fetch_size.3.gz
/usr/share/man/man3/cp_db_connection_set_read_result_set_at_once.3.gz
/usr/share/man/man3/cp_db_connection_unescape_binary.3.gz
/usr/share/man/man3/cp_db_connection_update.3.gz
/usr/share/man/man3/cp_db_init.3.gz
/usr/share/man/man3/cp_db_mysql.3.gz
/usr/share/man/man3/cp_db_postgres.3.gz
/usr/share/man/man3/cp_db_shutdown.3.gz
/usr/share/man/man3/cp_db_statement_set_binary.3.gz
/usr/share/man/man3/cp_dbms.3.gz
/usr/share/man/man3/cp_dbms_get_data_source.3.gz
/usr/share/man/man3/cp_dbms_get_data_source_prm.3.gz
/usr/share/man/man3/cp_dbms_load_driver.3.gz
/usr/share/man/man3/cp_hashlist.3.gz
/usr/share/man/man3/cp_hashlist_append.3.gz
/usr/share/man/man3/cp_hashlist_append_by_option.3.gz
/usr/share/man/man3/cp_hashlist_callback.3.gz
/usr/share/man/man3/cp_hashlist_contains.3.gz
/usr/share/man/man3/cp_hashlist_create.3.gz
/usr/share/man/man3/cp_hashlist_create_by_mode.3.gz
/usr/share/man/man3/cp_hashlist_create_by_option.3.gz
/usr/share/man/man3/cp_hashlist_create_iterator.3.gz
/usr/share/man/man3/cp_hashlist_destroy.3.gz
/usr/share/man/man3/cp_hashlist_destroy_by_option.3.gz
/usr/share/man/man3/cp_hashlist_destroy_custom.3.gz
/usr/share/man/man3/cp_hashlist_entry_get_key.3.gz
/usr/share/man/man3/cp_hashlist_entry_get_value.3.gz
/usr/share/man/man3/cp_hashlist_get.3.gz
/usr/share/man/man3/cp_hashlist_get_head.3.gz
/usr/share/man/man3/cp_hashlist_get_mode.3.gz
/usr/share/man/man3/cp_hashlist_get_tail.3.gz
/usr/share/man/man3/cp_hashlist_insert.3.gz
/usr/share/man/man3/cp_hashlist_insert_by_option.3.gz
/usr/share/man/man3/cp_hashlist_is_empty.3.gz
/usr/share/man/man3/cp_hashlist_item_count.3.gz
/usr/share/man/man3/cp_hashlist_iterator.3.gz
/usr/share/man/man3/cp_hashlist_iterator_append.3.gz
/usr/share/man/man3/cp_hashlist_iterator_curr.3.gz
/usr/share/man/man3/cp_hashlist_iterator_curr_key.3.gz
/usr/share/man/man3/cp_hashlist_iterator_curr_value.3.gz
/usr/share/man/man3/cp_hashlist_iterator_destroy.3.gz
/usr/share/man/man3/cp_hashlist_iterator_head.3.gz
/usr/share/man/man3/cp_hashlist_iterator_init.3.gz
/usr/share/man/man3/cp_hashlist_iterator_init_tail.3.gz
/usr/share/man/man3/cp_hashlist_iterator_insert.3.gz
/usr/share/man/man3/cp_hashlist_iterator_next.3.gz
/usr/share/man/man3/cp_hashlist_iterator_next_key.3.gz
/usr/share/man/man3/cp_hashlist_iterator_next_value.3.gz
/usr/share/man/man3/cp_hashlist_iterator_prev.3.gz
/usr/share/man/man3/cp_hashlist_iterator_prev_key.3.gz
/usr/share/man/man3/cp_hashlist_iterator_prev_value.3.gz
/usr/share/man/man3/cp_hashlist_iterator_release.3.gz
/usr/share/man/man3/cp_hashlist_iterator_remove.3.gz
/usr/share/man/man3/cp_hashlist_iterator_tail.3.gz
/usr/share/man/man3/cp_hashlist_iterator_to_key.3.gz
/usr/share/man/man3/cp_hashlist_lock.3.gz
/usr/share/man/man3/cp_hashlist_rdlock.3.gz
/usr/share/man/man3/cp_hashlist_remove.3.gz
/usr/share/man/man3/cp_hashlist_remove_by_option.3.gz
/usr/share/man/man3/cp_hashlist_remove_deep.3.gz
/usr/share/man/man3/cp_hashlist_remove_head.3.gz
/usr/share/man/man3/cp_hashlist_remove_head_by_option.3.gz
/usr/share/man/man3/cp_hashlist_remove_tail.3.gz
/usr/share/man/man3/cp_hashlist_remove_tail_by_option.3.gz
/usr/share/man/man3/cp_hashlist_set_max_fill_factor.3.gz
/usr/share/man/man3/cp_hashlist_set_min_fill_factor.3.gz
/usr/share/man/man3/cp_hashlist_set_min_size.3.gz
/usr/share/man/man3/cp_hashlist_set_mode.3.gz
/usr/share/man/man3/cp_hashlist_unlock.3.gz
/usr/share/man/man3/cp_hashlist_unset_mode.3.gz
/usr/share/man/man3/cp_hashlist_wrlock.3.gz
/usr/share/man/man3/cp_hashtable.3.gz
/usr/share/man/man3/cp_hashtable_contains.3.gz
/usr/share/man/man3/cp_hashtable_count.3.gz
/usr/share/man/man3/cp_hashtable_create.3.gz
/usr/share/man/man3/cp_hashtable_create_by_mode.3.gz
/usr/share/man/man3/cp_hashtable_create_by_option.3.gz
/usr/share/man/man3/cp_hashtable_create_copy.3.gz
/usr/share/man/man3/cp_hashtable_create_copy_mode.3.gz
/usr/share/man/man3/cp_hashtable_destroy.3.gz
/usr/share/man/man3/cp_hashtable_destroy_custom.3.gz
/usr/share/man/man3/cp_hashtable_destroy_deep.3.gz
/usr/share/man/man3/cp_hashtable_destroy_shallow.3.gz
/usr/share/man/man3/cp_hashtable_get.3.gz
/usr/share/man/man3/cp_hashtable_get_by_option.3.gz
/usr/share/man/man3/cp_hashtable_get_keys.3.gz
/usr/share/man/man3/cp_hashtable_get_values.3.gz
/usr/share/man/man3/cp_hashtable_is_empty.3.gz
/usr/share/man/man3/cp_hashtable_lock.3.gz
/usr/share/man/man3/cp_hashtable_put.3.gz
/usr/share/man/man3/cp_hashtable_put_by_option.3.gz
/usr/share/man/man3/cp_hashtable_put_copy.3.gz
/usr/share/man/man3/cp_hashtable_put_safe.3.gz
/usr/share/man/man3/cp_hashtable_rdlock.3.gz
/usr/share/man/man3/cp_hashtable_remove.3.gz
/usr/share/man/man3/cp_hashtable_remove_all.3.gz
/usr/share/man/man3/cp_hashtable_remove_deep.3.gz
/usr/share/man/man3/cp_hashtable_set_max_fill_factor.3.gz
/usr/share/man/man3/cp_hashtable_set_min_fill_factor.3.gz
/usr/share/man/man3/cp_hashtable_set_min_size.3.gz
/usr/share/man/man3/cp_hashtable_set_mode.3.gz
/usr/share/man/man3/cp_hashtable_unlock.3.gz
/usr/share/man/man3/cp_hashtable_unset_mode.3.gz
/usr/share/man/man3/cp_hashtable_wrlock.3.gz
/usr/share/man/man3/cp_heap.3.gz
/usr/share/man/man3/cp_heap_callback.3.gz
/usr/share/man/man3/cp_heap_contract.3.gz
/usr/share/man/man3/cp_heap_count.3.gz
/usr/share/man/man3/cp_heap_create.3.gz
/usr/share/man/man3/cp_heap_create_by_option.3.gz
/usr/share/man/man3/cp_heap_destroy.3.gz
/usr/share/man/man3/cp_heap_get_mode.3.gz
/usr/share/man/man3/cp_heap_lock.3.gz
/usr/share/man/man3/cp_heap_peek.3.gz
/usr/share/man/man3/cp_heap_pop.3.gz
/usr/share/man/man3/cp_heap_push.3.gz
/usr/share/man/man3/cp_heap_set_mode.3.gz
/usr/share/man/man3/cp_heap_size.3.gz
/usr/share/man/man3/cp_heap_unlock.3.gz
/usr/share/man/man3/cp_heap_unset_mode.3.gz
/usr/share/man/man3/cp_http_init.3.gz
/usr/share/man/man3/cp_http_request.3.gz
/usr/share/man/man3/cp_http_request_dump.3.gz
/usr/share/man/man3/cp_http_request_get_header.3.gz
/usr/share/man/man3/cp_http_request_get_parameter.3.gz
/usr/share/man/man3/cp_http_request_get_session.3.gz
/usr/share/man/man3/cp_http_response.3.gz
/usr/share/man/man3/cp_http_response_set_body.3.gz
/usr/share/man/man3/cp_http_response_set_connection_policy.3.gz
/usr/share/man/man3/cp_http_response_set_content.3.gz
/usr/share/man/man3/cp_http_response_set_content_type.3.gz
/usr/share/man/man3/cp_http_response_set_content_type_string.3.gz
/usr/share/man/man3/cp_http_response_set_cookie.3.gz
/usr/share/man/man3/cp_http_response_set_header.3.gz
/usr/share/man/man3/cp_http_response_set_status.3.gz
/usr/share/man/man3/cp_http_service.3.gz
/usr/share/man/man3/cp_http_service_create.3.gz
/usr/share/man/man3/cp_http_service_delete.3.gz
/usr/share/man/man3/cp_http_session.3.gz
/usr/share/man/man3/cp_http_session_get.3.gz
/usr/share/man/man3/cp_http_session_is_fresh.3.gz
/usr/share/man/man3/cp_http_session_set.3.gz
/usr/share/man/man3/cp_http_session_set_dtr.3.gz
/usr/share/man/man3/cp_http_session_set_validity.3.gz
/usr/share/man/man3/cp_http_shutdown.3.gz
/usr/share/man/man3/cp_httpclient.3.gz
/usr/share/man/man3/cp_httpclient_allow_redirects.3.gz
/usr/share/man/man3/cp_httpclient_create.3.gz
/usr/share/man/man3/cp_httpclient_create_proxy.3.gz
/usr/share/man/man3/cp_httpclient_create_proxy_ssl.3.gz
/usr/share/man/man3/cp_httpclient_create_ssl.3.gz
/usr/share/man/man3/cp_httpclient_ctl.3.gz
/usr/share/man/man3/cp_httpclient_ctl_create.3.gz
/usr/share/man/man3/cp_httpclient_ctl_destroy.3.gz
/usr/share/man/man3/cp_httpclient_ctl_get_pollfds.3.gz
/usr/share/man/man3/cp_httpclient_ctl_get_read_fd_set.3.gz
/usr/share/man/man3/cp_httpclient_ctl_get_write_fd_set.3.gz
/usr/share/man/man3/cp_httpclient_destroy.3.gz
/usr/share/man/man3/cp_httpclient_drop_headers.3.gz
/usr/share/man/man3/cp_httpclient_drop_parameters.3.gz
/usr/share/man/man3/cp_httpclient_fetch.3.gz
/usr/share/man/man3/cp_httpclient_fetch_ctl.3.gz
/usr/share/man/man3/cp_httpclient_fetch_ctl_exec.3.gz
/usr/share/man/man3/cp_httpclient_fetch_nb.3.gz
/usr/share/man/man3/cp_httpclient_fetch_nb_exec.3.gz
/usr/share/man/man3/cp_httpclient_init.3.gz
/usr/share/man/man3/cp_httpclient_reopen.3.gz
/usr/share/man/man3/cp_httpclient_result.3.gz
/usr/share/man/man3/cp_httpclient_set_auto_drop_headers.3.gz
/usr/share/man/man3/cp_httpclient_set_auto_drop_parameters.3.gz
/usr/share/man/man3/cp_httpclient_set_cookie_jar.3.gz
/usr/share/man/man3/cp_httpclient_set_header.3.gz
/usr/share/man/man3/cp_httpclient_set_http_version.3.gz
/usr/share/man/man3/cp_httpclient_set_max_redirects.3.gz
/usr/share/man/man3/cp_httpclient_set_paremeter.3.gz
/usr/share/man/man3/cp_httpclient_set_request_type.3.gz
/usr/share/man/man3/cp_httpclient_set_retry.3.gz
/usr/share/man/man3/cp_httpclient_set_timeout.3.gz
/usr/share/man/man3/cp_httpclient_set_user_agent.3.gz
/usr/share/man/man3/cp_httpclient_shutdown.3.gz
/usr/share/man/man3/cp_httpsocket.3.gz
/usr/share/man/man3/cp_httpsocket_create.3.gz
/usr/share/man/man3/cp_httpsocket_create_ssl.3.gz
/usr/share/man/man3/cp_httpsocket_delete.3.gz
/usr/share/man/man3/cp_httpsocket_listen.3.gz
/usr/share/man/man3/cp_httpsocket_register_service.3.gz
/usr/share/man/man3/cp_httpsocket_stop_all.3.gz
/usr/share/man/man3/cp_httpsocket_unregister_service.3.gz
/usr/share/man/man3/cp_list.3.gz
/usr/share/man/man3/cp_list_append.3.gz
/usr/share/man/man3/cp_list_callback.3.gz
/usr/share/man/man3/cp_list_create.3.gz
/usr/share/man/man3/cp_list_create_iterator.3.gz
/usr/share/man/man3/cp_list_create_list.3.gz
/usr/share/man/man3/cp_list_create_nosync.3.gz
/usr/share/man/man3/cp_list_destroy.3.gz
/usr/share/man/man3/cp_list_destroy_by_option.3.gz
/usr/share/man/man3/cp_list_destroy_custom.3.gz
/usr/share/man/man3/cp_list_get_head.3.gz
/usr/share/man/man3/cp_list_get_tail.3.gz
/usr/share/man/man3/cp_list_insert.3.gz
/usr/share/man/man3/cp_list_insert_after.3.gz
/usr/share/man/man3/cp_list_insert_before.3.gz
/usr/share/man/man3/cp_list_is_empty.3.gz
/usr/share/man/man3/cp_list_item_count.3.gz
/usr/share/man/man3/cp_list_iterator.3.gz
/usr/share/man/man3/cp_list_iterator_append.3.gz
/usr/share/man/man3/cp_list_iterator_curr.3.gz
/usr/share/man/man3/cp_list_iterator_destroy.3.gz
/usr/share/man/man3/cp_list_iterator_head.3.gz
/usr/share/man/man3/cp_list_iterator_init.3.gz
/usr/share/man/man3/cp_list_iterator_init_tail.3.gz
/usr/share/man/man3/cp_list_iterator_insert.3.gz
/usr/share/man/man3/cp_list_iterator_next.3.gz
/usr/share/man/man3/cp_list_iterator_prev.3.gz
/usr/share/man/man3/cp_list_iterator_release.3.gz
/usr/share/man/man3/cp_list_iterator_remove.3.gz
/usr/share/man/man3/cp_list_iterator_tail.3.gz
/usr/share/man/man3/cp_list_lock.3.gz
/usr/share/man/man3/cp_list_rdlock.3.gz
/usr/share/man/man3/cp_list_remove.3.gz
/usr/share/man/man3/cp_list_remove_head.3.gz
/usr/share/man/man3/cp_list_remove_tail.3.gz
/usr/share/man/man3/cp_list_search.3.gz
/usr/share/man/man3/cp_list_unlock.3.gz
/usr/share/man/man3/cp_list_wrlock.3.gz
/usr/share/man/man3/cp_mempool.3.gz
/usr/share/man/man3/cp_mempool_alloc.3.gz
/usr/share/man/man3/cp_mempool_calloc.3.gz
/usr/share/man/man3/cp_mempool_create.3.gz
/usr/share/man/man3/cp_mempool_create_by_option.3.gz
/usr/share/man/man3/cp_mempool_destroy.3.gz
/usr/share/man/man3/cp_mempool_free.3.gz
/usr/share/man/man3/cp_mempool_inc_refcount.3.gz
/usr/share/man/man3/cp_multimap.3.gz
/usr/share/man/man3/cp_multimap_callback.3.gz
/usr/share/man/man3/cp_multimap_callback_by_index.3.gz
/usr/share/man/man3/cp_multimap_callback_postorder.3.gz
/usr/share/man/man3/cp_multimap_callback_preorder.3.gz
/usr/share/man/man3/cp_multimap_contains.3.gz
/usr/share/man/man3/cp_multimap_count.3.gz
/usr/share/man/man3/cp_multimap_create.3.gz
/usr/share/man/man3/cp_multimap_create_by_option.3.gz
/usr/share/man/man3/cp_multimap_create_index.3.gz
/usr/share/man/man3/cp_multimap_destroy.3.gz
/usr/share/man/man3/cp_multimap_destroy_custom.3.gz
/usr/share/man/man3/cp_multimap_find.3.gz
/usr/share/man/man3/cp_multimap_find_by_index.3.gz
/usr/share/man/man3/cp_multimap_get.3.gz
/usr/share/man/man3/cp_multimap_get_by_index.3.gz
/usr/share/man/man3/cp_multimap_get_mode.3.gz
/usr/share/man/man3/cp_multimap_insert.3.gz
/usr/share/man/man3/cp_multimap_lock.3.gz
/usr/share/man/man3/cp_multimap_rdlock.3.gz
/usr/share/man/man3/cp_multimap_reindex.3.gz
/usr/share/man/man3/cp_multimap_remove.3.gz
/usr/share/man/man3/cp_multimap_remove_by_index.3.gz
/usr/share/man/man3/cp_multimap_set_mode.3.gz
/usr/share/man/man3/cp_multimap_share_mempool.3.gz
/usr/share/man/man3/cp_multimap_size.3.gz
/usr/share/man/man3/cp_multimap_unlock.3.gz
/usr/share/man/man3/cp_multimap_unset_mode.3.gz
/usr/share/man/man3/cp_multimap_use_mempool.3.gz
/usr/share/man/man3/cp_multimap_wrlock.3.gz
/usr/share/man/man3/cp_mysql_data_source.3.gz
/usr/share/man/man3/cp_narytree.3.gz
/usr/share/man/man3/cp_narytree_callback.3.gz
/usr/share/man/man3/cp_narytree_contains.3.gz
/usr/share/man/man3/cp_narytree_count.3.gz
/usr/share/man/man3/cp_narytree_create.3.gz
/usr/share/man/man3/cp_narytree_create_by_option.3.gz
/usr/share/man/man3/cp_narytree_delete.3.gz
/usr/share/man/man3/cp_narytree_destroy.3.gz
/usr/share/man/man3/cp_narytree_destroy_custom.3.gz
/usr/share/man/man3/cp_narytree_get.3.gz
/usr/share/man/man3/cp_narytree_get_mode.3.gz
/usr/share/man/man3/cp_narytree_insert.3.gz
/usr/share/man/man3/cp_narytree_lock.3.gz
/usr/share/man/man3/cp_narytree_rdlock.3.gz
/usr/share/man/man3/cp_narytree_set_mode.3.gz
/usr/share/man/man3/cp_narytree_unlock.3.gz
/usr/share/man/man3/cp_narytree_unset_mode.3.gz
/usr/share/man/man3/cp_narytree_wrlock.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_create.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_destroy.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_get.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_get_nb.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_get_stoppable.3.gz
/usr/share/man/man3/cp_pooled_thread_client_interface_get_stoppable_nb.3.gz
/usr/share/man/man3/cp_pooled_thread_client_negociate.3.gz
/usr/share/man/man3/cp_pooled_thread_scheduler.3.gz
/usr/share/man/man3/cp_pooled_thread_scheduler_create.3.gz
/usr/share/man/man3/cp_pooled_thread_scheduler_destroy.3.gz
/usr/share/man/man3/cp_pooled_thread_scheduler_register_client.3.gz
/usr/share/man/man3/cp_postgres_data_source.3.gz
/usr/share/man/man3/cp_priority_list.3.gz
/usr/share/man/man3/cp_priority_list_create.3.gz
/usr/share/man/man3/cp_priority_list_create_by_option.3.gz
/usr/share/man/man3/cp_priority_list_destroy.3.gz
/usr/share/man/man3/cp_priority_list_destroy_by_option.3.gz
/usr/share/man/man3/cp_priority_list_get_next.3.gz
/usr/share/man/man3/cp_priority_list_get_next_by_option.3.gz
/usr/share/man/man3/cp_priority_list_insert.3.gz
/usr/share/man/man3/cp_priority_list_insert_by_option.3.gz
/usr/share/man/man3/cp_priority_list_is_empty.3.gz
/usr/share/man/man3/cp_priority_list_item_count.3.gz
/usr/share/man/man3/cp_priority_list_lock.3.gz
/usr/share/man/man3/cp_priority_list_rdlock.3.gz
/usr/share/man/man3/cp_priority_list_unlock.3.gz
/usr/share/man/man3/cp_priority_list_wrlock.3.gz
/usr/share/man/man3/cp_rbtree.3.gz
/usr/share/man/man3/cp_rbtree_callback.3.gz
/usr/share/man/man3/cp_rbtree_callback_postorder.3.gz
/usr/share/man/man3/cp_rbtree_callback_preorder.3.gz
/usr/share/man/man3/cp_rbtree_contains.3.gz
/usr/share/man/man3/cp_rbtree_count.3.gz
/usr/share/man/man3/cp_rbtree_create.3.gz
/usr/share/man/man3/cp_rbtree_create_by_option.3.gz
/usr/share/man/man3/cp_rbtree_delete.3.gz
/usr/share/man/man3/cp_rbtree_destroy.3.gz
/usr/share/man/man3/cp_rbtree_destroy_custom.3.gz
/usr/share/man/man3/cp_rbtree_get.3.gz
/usr/share/man/man3/cp_rbtree_get_mode.3.gz
/usr/share/man/man3/cp_rbtree_insert.3.gz
/usr/share/man/man3/cp_rbtree_lock.3.gz
/usr/share/man/man3/cp_rbtree_rdlock.3.gz
/usr/share/man/man3/cp_rbtree_set_mode.3.gz
/usr/share/man/man3/cp_rbtree_unlock.3.gz
/usr/share/man/man3/cp_rbtree_unset_mode.3.gz
/usr/share/man/man3/cp_rbtree_wrlock.3.gz
/usr/share/man/man3/cp_result_set.3.gz
/usr/share/man/man3/cp_result_set_autodispose.3.gz
/usr/share/man/man3/cp_result_set_destroy.3.gz
/usr/share/man/man3/cp_result_set_field_count.3.gz
/usr/share/man/man3/cp_result_set_get_field_type.3.gz
/usr/share/man/man3/cp_result_set_get_field_types.3.gz
/usr/share/man/man3/cp_result_set_get_header.3.gz
/usr/share/man/man3/cp_result_set_get_headers.3.gz
/usr/share/man/man3/cp_result_set_is_binary.3.gz
/usr/share/man/man3/cp_result_set_next.3.gz
/usr/share/man/man3/cp_result_set_release_row.3.gz
/usr/share/man/man3/cp_result_set_row_count.3.gz
/usr/share/man/man3/cp_rtrie.3.gz
/usr/share/man/man3/cp_rtrie_add.3.gz
/usr/share/man/man3/cp_rtrie_create.3.gz
/usr/share/man/man3/cp_rtrie_create_trie.3.gz
/usr/share/man/man3/cp_rtrie_destroy.3.gz
/usr/share/man/man3/cp_rtrie_exact_match.3.gz
/usr/share/man/man3/cp_rtrie_fetch_matches.3.gz
/usr/share/man/man3/cp_rtrie_get_mode.3.gz
/usr/share/man/man3/cp_rtrie_lock.3.gz
/usr/share/man/man3/cp_rtrie_prefix_match.3.gz
/usr/share/man/man3/cp_rtrie_rdlock.3.gz
/usr/share/man/man3/cp_rtrie_remove.3.gz
/usr/share/man/man3/cp_rtrie_set_mode.3.gz
/usr/share/man/man3/cp_rtrie_unlock.3.gz
/usr/share/man/man3/cp_rtrie_unset_mode.3.gz
/usr/share/man/man3/cp_rtrie_wrlock.3.gz
/usr/share/man/man3/cp_shared_mempool.3.gz
/usr/share/man/man3/cp_shared_mempool_alloc.3.gz
/usr/share/man/man3/cp_shared_mempool_calloc.3.gz
/usr/share/man/man3/cp_shared_mempool_create.3.gz
/usr/share/man/man3/cp_shared_mempool_create_by_option.3.gz
/usr/share/man/man3/cp_shared_mempool_destroy.3.gz
/usr/share/man/man3/cp_shared_mempool_free.3.gz
/usr/share/man/man3/cp_shared_mempool_register.3.gz
/usr/share/man/man3/cp_socket.3.gz
/usr/share/man/man3/cp_socket_connection_close.3.gz
/usr/share/man/man3/cp_socket_create.3.gz
/usr/share/man/man3/cp_socket_create_ssl.3.gz
/usr/share/man/man3/cp_socket_delete.3.gz
/usr/share/man/man3/cp_socket_init.3.gz
/usr/share/man/man3/cp_socket_listen.3.gz
/usr/share/man/man3/cp_socket_select.3.gz
/usr/share/man/man3/cp_socket_set_backlog.3.gz
/usr/share/man/man3/cp_socket_set_delay.3.gz
/usr/share/man/man3/cp_socket_set_delay_sec.3.gz
/usr/share/man/man3/cp_socket_set_delay_usec.3.gz
/usr/share/man/man3/cp_socket_set_owner.3.gz
/usr/share/man/man3/cp_socket_set_poolsize_max.3.gz
/usr/share/man/man3/cp_socket_set_poolsize_min.3.gz
/usr/share/man/man3/cp_socket_shutdown.3.gz
/usr/share/man/man3/cp_socket_stop_all.3.gz
/usr/share/man/man3/cp_sorted_hash.3.gz
/usr/share/man/man3/cp_sorted_hash_callback.3.gz
/usr/share/man/man3/cp_sorted_hash_contains.3.gz
/usr/share/man/man3/cp_sorted_hash_count.3.gz
/usr/share/man/man3/cp_sorted_hash_create.3.gz
/usr/share/man/man3/cp_sorted_hash_create_by_mode.3.gz
/usr/share/man/man3/cp_sorted_hash_delete.3.gz
/usr/share/man/man3/cp_sorted_hash_destroy.3.gz
/usr/share/man/man3/cp_sorted_hash_destroy_custom.3.gz
/usr/share/man/man3/cp_sorted_hash_get.3.gz
/usr/share/man/man3/cp_sorted_hash_get_mode.3.gz
/usr/share/man/man3/cp_sorted_hash_insert.3.gz
/usr/share/man/man3/cp_sorted_hash_lock.3.gz
/usr/share/man/man3/cp_sorted_hash_rdlock.3.gz
/usr/share/man/man3/cp_sorted_hash_set_mode.3.gz
/usr/share/man/man3/cp_sorted_hash_unlock.3.gz
/usr/share/man/man3/cp_sorted_hash_unset_mode.3.gz
/usr/share/man/man3/cp_sorted_hash_wrlock.3.gz
/usr/share/man/man3/cp_splaytree.3.gz
/usr/share/man/man3/cp_splaytree_callback.3.gz
/usr/share/man/man3/cp_splaytree_contains.3.gz
/usr/share/man/man3/cp_splaytree_count.3.gz
/usr/share/man/man3/cp_splaytree_create.3.gz
/usr/share/man/man3/cp_splaytree_create_by_option.3.gz
/usr/share/man/man3/cp_splaytree_delete.3.gz
/usr/share/man/man3/cp_splaytree_destroy.3.gz
/usr/share/man/man3/cp_splaytree_destroy_custom.3.gz
/usr/share/man/man3/cp_splaytree_get.3.gz
/usr/share/man/man3/cp_splaytree_get_mode.3.gz
/usr/share/man/man3/cp_splaytree_insert.3.gz
/usr/share/man/man3/cp_splaytree_lock.3.gz
/usr/share/man/man3/cp_splaytree_rdlock.3.gz
/usr/share/man/man3/cp_splaytree_set_mode.3.gz
/usr/share/man/man3/cp_splaytree_unlock.3.gz
/usr/share/man/man3/cp_splaytree_unset_mode.3.gz
/usr/share/man/man3/cp_splaytree_wrlock.3.gz
/usr/share/man/man3/cp_string.3.gz
/usr/share/man/man3/cp_string_cat.3.gz
/usr/share/man/man3/cp_string_cat_bin.3.gz
/usr/share/man/man3/cp_string_cmp.3.gz
/usr/share/man/man3/cp_string_cpy.3.gz
/usr/share/man/man3/cp_string_create.3.gz
/usr/share/man/man3/cp_string_cstrcat.3.gz
/usr/share/man/man3/cp_string_cstrcpy.3.gz
/usr/share/man/man3/cp_string_cstrdup.3.gz
/usr/share/man/man3/cp_string_delete.3.gz
/usr/share/man/man3/cp_string_dump.3.gz
/usr/share/man/man3/cp_string_dup.3.gz
/usr/share/man/man3/cp_string_len.3.gz
/usr/share/man/man3/cp_string_read.3.gz
/usr/share/man/man3/cp_string_reset.3.gz
/usr/share/man/man3/cp_string_tocstr.3.gz
/usr/share/man/man3/cp_string_write.3.gz
/usr/share/man/man3/cp_thread.3.gz
/usr/share/man/man3/cp_thread_create.3.gz
/usr/share/man/man3/cp_thread_detach.3.gz
/usr/share/man/man3/cp_thread_join.3.gz
/usr/share/man/man3/cp_thread_pool.3.gz
/usr/share/man/man3/cp_thread_pool_count_available.3.gz
/usr/share/man/man3/cp_thread_pool_create.3.gz
/usr/share/man/man3/cp_thread_pool_destroy.3.gz
/usr/share/man/man3/cp_thread_pool_get.3.gz
/usr/share/man/man3/cp_thread_pool_get_nb.3.gz
/usr/share/man/man3/cp_thread_pool_get_stoppable.3.gz
/usr/share/man/man3/cp_thread_pool_get_stoppable_nb.3.gz
/usr/share/man/man3/cp_thread_pool_stop.3.gz
/usr/share/man/man3/cp_timestampz.3.gz
/usr/share/man/man3/cp_timestampz_create.3.gz
/usr/share/man/man3/cp_timestampz_create_prm.3.gz
/usr/share/man/man3/cp_timestampz_destroy.3.gz
/usr/share/man/man3/cp_timestampz_localtime.3.gz
/usr/share/man/man3/cp_trie.3.gz
/usr/share/man/man3/cp_trie_add.3.gz
/usr/share/man/man3/cp_trie_create.3.gz
/usr/share/man/man3/cp_trie_destroy.3.gz
/usr/share/man/man3/cp_trie_exact_match.3.gz
/usr/share/man/man3/cp_trie_get_mode.3.gz
/usr/share/man/man3/cp_trie_lock.3.gz
/usr/share/man/man3/cp_trie_match.3.gz
/usr/share/man/man3/cp_trie_rdlock.3.gz
/usr/share/man/man3/cp_trie_remove.3.gz
/usr/share/man/man3/cp_trie_set_mode.3.gz
/usr/share/man/man3/cp_trie_unlock.3.gz
/usr/share/man/man3/cp_trie_unset_mode.3.gz
/usr/share/man/man3/cp_trie_wrlock.3.gz
/usr/share/man/man3/cp_vector.3.gz
/usr/share/man/man3/cp_vector_add_element.3.gz
/usr/share/man/man3/cp_vector_create.3.gz
/usr/share/man/man3/cp_vector_create_by_option.3.gz
/usr/share/man/man3/cp_vector_destroy.3.gz
/usr/share/man/man3/cp_vector_destroy_custom.3.gz
/usr/share/man/man3/cp_vector_element_at.3.gz
/usr/share/man/man3/cp_vector_set_element.3.gz
/usr/share/man/man3/cp_vector_size.3.gz
/usr/share/man/man3/cp_wtrie.3.gz
/usr/share/man/man3/cp_wtrie_add.3.gz
/usr/share/man/man3/cp_wtrie_create.3.gz
/usr/share/man/man3/cp_wtrie_create_trie.3.gz
/usr/share/man/man3/cp_wtrie_destroy.3.gz
/usr/share/man/man3/cp_wtrie_exact_match.3.gz
/usr/share/man/man3/cp_wtrie_fetch_matches.3.gz
/usr/share/man/man3/cp_wtrie_get_mode.3.gz
/usr/share/man/man3/cp_wtrie_lock.3.gz
/usr/share/man/man3/cp_wtrie_prefix_match.3.gz
/usr/share/man/man3/cp_wtrie_rdlock.3.gz
/usr/share/man/man3/cp_wtrie_remove.3.gz
/usr/share/man/man3/cp_wtrie_set_mode.3.gz
/usr/share/man/man3/cp_wtrie_unlock.3.gz
/usr/share/man/man3/cp_wtrie_unset_mode.3.gz
/usr/share/man/man3/cp_wtrie_wrlock.3.gz
/usr/share/man/man3/cprops.3.gz
/usr/share/man/man3/cstr_to_bstr.3.gz
/usr/share/man/man3/libcprops.3.gz

%changelog
* Sun Sep 16 2018 Build <chris.olido@gmail.com>

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /root/rpmbuild/BUILD
rm -rf libcprops-0.1.12.zip
unzip /root/rpmbuild/SOURCES/libcprops-0.1.12.zip | tar -xvf -
if [ $? -ne 0 ]; then
  exit $?
fi
cd libcprops-0.1.12
cd /root/rpmbuild/BUILD/libcprops-0.1.12
chown -R root.root .
chmod -R a+rX,g-w,o-w .
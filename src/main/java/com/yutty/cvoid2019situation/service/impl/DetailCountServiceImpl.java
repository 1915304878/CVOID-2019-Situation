package com.yutty.cvoid2019situation.service.impl;


import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.yutty.cvoid2019situation.entity.Detailcount;
import com.yutty.cvoid2019situation.mapper.DetailCountMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import com.yutty.cvoid2019situation.service.DetailCountService;

@Service
@Slf4j
public class DetailCountServiceImpl extends ServiceImpl<DetailCountMapper, Detailcount> implements DetailCountService {

}
